import torch
import argparse
import time
from torch.utils.data import TensorDataset, DataLoader
from dataset_maker import make_dataset
from attacker_maker import make_attacker
from model_maker import make_model
from detector_maker import make_detector
from pytorch_ood.utils import OODMetrics
from torchmetrics.functional.classification import (
    binary_auroc,
    binary_precision_recall_curve,
    binary_roc,
)
import os


parser = argparse.ArgumentParser(description='config')
parser.add_argument('--attack_data', default='FGSM_cifar10', type=str)
parser.add_argument('--model', default='WideResNet', type=str)
parser.add_argument('--detector', default='Entropy', type=str)
args = vars(parser.parse_args())

def test_detector(detector, dataloader, metrics, device):
    for images, labels in dataloader:
        metrics.update(detector(images.to(device)), labels.to(device))



def main():
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(device)

    attack_data = args['attack_data']
    attack_name, dataset_name = attack_data.split('_')
    detector_name = args['detector']
    model_name = args['model']

    print(attack_name)
    print(dataset_name)

    # generate model
    model = make_model(model_name, device)
    print('Model generated:{}.'.format(model_name))

    # load attack data
    data_dict = torch.load('G:/.shortcut-targets-by-id/1u1nyH7YGtWM2j7D9r9JkwmD-pTuwnODw/Adversarial Learning/output/attacked_data/{}.pt'.format(attack_data))
    #train_attacked_data = data_dict['train_images']
    #train_label_data = data_dict['train_labels']
    test_attacked_data = data_dict['test_images']
    test_label_data = data_dict['test_labels']

    #attacked_train_dataset = TensorDataset(train_attacked_data, train_label_data)
    attacked_test_dataset = TensorDataset(test_attacked_data, test_label_data)
    #attacked_train_loader = DataLoader(attacked_train_dataset, batch_size=128, shuffle=True)
    attacked_test_loader = DataLoader(attacked_test_dataset, batch_size=128, shuffle=True)


    train_loader, test_loader = make_dataset(dataset_name)
    print('attacked_test_loader and test_loader generated.')

    #for image,label in test_loader:
    #    print(image[0],label[0])

    # generate detector
    detector = make_detector(detector_name, model, train_loader, device)
    print('detector generated: {}.'.format(detector_name))

    start_time = time.time()
    print(f"> Evaluating detector: {detector_name} under attack: {attack_name}, on dataset: {dataset_name}")
    
    metrics = OODMetrics()

    # test_detector(detector, attacked_train_loader, metrics, device)
    # print('attacked_train_loader finished')
    # test_detector(detector, train_loader, metrics, device)
    # print('train_loader finished')
    test_detector(detector, attacked_test_loader, metrics, device)
    # print('attacked_test_loader finished')
    test_detector(detector, test_loader, metrics, device)
    # print('test_loader finished')


    # ROC Curves
    data_dict = {}
    labels = metrics.buffer.get("labels").view(-1)
    scores = metrics.buffer.get("scores").view(-1)
    p, r, t = binary_roc(scores, labels)
    data_dict['originalROC'] = p, r

    in_indices = (labels == False)
    out_indices = (labels == True)
    #scores_in = scores[in_indices]
    in_scores = scores[in_indices]
    out_scores = scores[out_indices]
    data_dict['original_scores'] = (in_scores, out_scores)
    in_scores, _ = torch.sort(in_scores, stable=True)
    mid_in_scores = in_scores[in_scores.size()[0] // 2]
    scores = torch.abs(scores - mid_in_scores)
    in_scores = torch.abs(in_scores - mid_in_scores)
    out_scores = torch.abs(out_scores - mid_in_scores)
    data_dict['modified_scores'] = (in_scores, out_scores)

    p, r, t = binary_roc(scores, labels)
    data_dict['modifiedROC'] = p, r


    end_time = time.time()
    processing_time_seconds = end_time - start_time
    print(f"----> Processing time: {processing_time_seconds} seconds")
    print('Result:\n',metrics.compute())
    data_dict['data'] = metrics.compute()


    directory_path = './output/detector_result/'
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    file_name = os.path.join(directory_path, '{}_{}_{}.pt'.format(detector_name, attack_name, dataset_name))
    torch.save(data_dict, file_name)
    print('Data generated at '+ file_name)


    


if __name__ == '__main__':
    main()

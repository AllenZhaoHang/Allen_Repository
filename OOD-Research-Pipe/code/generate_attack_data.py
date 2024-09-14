import torch
#print(torch.__version__)
import argparse
import time
import os
from dataset_maker import make_dataset
from attacker_maker import make_attacker
from model_maker import make_model

directory_path = os.path.join('.', 'output', 'attacked_data')

if not os.path.exists(directory_path):
    os.makedirs(directory_path)

parser = argparse.ArgumentParser(description='config')
parser.add_argument('--attack_name', default='FGSM', type=str)
parser.add_argument('--dataset', default='cifar10', type=str)
parser.add_argument('--model', default='WideResNet', type=str)
args = vars(parser.parse_args())


def seconds2hms(total_time):
    hours, remainder = divmod(total_time, 3600)
    minutes, seconds = divmod(remainder, 60)
    return hours, minutes, seconds


def Estimate_process_time(train_loader, test_loader, attacker):
    length = len(train_loader) + len(test_loader)
    #print(length)
    for i, inputs in enumerate(train_loader):
        t_start = time.time()
        image, label = inputs
        #batch_len = len(label)
        image_attacked = attacker(image, label)
        t_end = time.time()
        break

    hours, minutes, seconds = seconds2hms((t_end-t_start) * length )
    print(f"Estimate_process_time: {int(hours)} hours {int(minutes)} minutes {int(seconds)} seconds")


def main():
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(device)

    attack_name = args['attack_name']
    dataset = args['dataset']
    model_name = args['model']

    model = make_model(model_name, device)

    print('Model generated.')

    attacker = make_attacker(attack_name, model)
    train_loader, test_loader = make_dataset(dataset, batch_size=128)

    print('Attacker {} generated.'.format(attack_name))

    train_attacked_data = [] #torch.tensor([]).to(device)
    train_label_data = [] #torch.tensor([]).to(device)

    start_time = time.time()


    # Estimate running time
    #Estimate_process_time(train_loader, test_loader, attacker)

    #return


    print('Modifing train data')
    for i, inputs in enumerate(train_loader):
        image, label = inputs
        image_attacked = attacker(image, label)
        train_attacked_data.append(image_attacked)
        train_label_data.append(label)


    train_attacked_data = torch.cat(train_attacked_data, dim=0)
    train_label_data = torch.cat(train_label_data, dim=0)


    test_attacked_data = [] #torch.tensor([]).to(device)
    test_label_data = [] # torch.tensor([]).to(device)

    print('Modifing test data')
    for i, inputs in enumerate(test_loader):
        image, label = inputs
        image_attacked = attacker(image, label)
        test_attacked_data.append(image_attacked)
        test_label_data.append(-1*torch.ones_like(label))

        #test_attacked_data = torch.cat((test_attacked_data, image_attacked.to(device)), dim=0)
        #test_label_data = torch.cat((test_label_data, -1*torch.ones_like(label).to(device)), dim=0)
    test_attacked_data = torch.cat(test_attacked_data, dim=0)
    test_label_data = torch.cat(test_label_data, dim=0)

    data_dict = {
        'train_images': train_attacked_data,
        'train_labels': train_label_data,
        'test_images': test_attacked_data,
        'test_labels': test_label_data,
    }

    file_name = os.path.join(directory_path, '{}_{}.pt'.format(attack_name, dataset))
    torch.save(data_dict, file_name)
    print('Data generated at '+file_name)

    end_time = time.time()
    processing_time_seconds = end_time - start_time
    hours, minutes, seconds = seconds2hms(processing_time_seconds)
    print(f"----> Processing time: {int(hours)} hours {int(minutes)} minutes {int(seconds)} seconds")


if __name__ == '__main__':
    main()

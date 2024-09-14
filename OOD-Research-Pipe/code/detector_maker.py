from pytorch_ood.detector import (ODIN, EnergyBased, Entropy, KLMatching, Mahalanobis, MaxLogit, MaxSoftmax,
    ViM, RMD, DICE, SHE, MCD, TemperatureScaling, OpenMax, KNN, ASH, ReAct) # RMD, DICE, SHE, MCD, OpenMax
#from torchvision.datasets import CIFAR10
#import torchvision.transforms as tvt
#from pytorch_ood.utils import OODMetrics, ToRGB, ToUnknown

'''
mean=[0.485, 0.456, 0.406]
std=[0.229, 0.224, 0.225]
trans = tvt.Compose([tvt.Resize(size=(32, 32)), ToRGB(), tvt.ToTensor(), tvt.Normalize(std=std, mean=mean)])
'''
#detector_list = ["ReAct", "OpenMax", "TemperatureScaling", "KNN", 'ODIN', 'EnergyBased', 'Entropy', 'KLMatching', 'Mahalanobis', 'Mahalanobis+ODIN',
#                 'MaxLogit','ViM', 'RMD', 'DICE', 'SHE', "MSP", "MCD", "ASH"]

#dataset_in_train = CIFAR10(root="data", train=True, transform=trans, download=True)
#train_loader = DataLoader(dataset_in_train, batch_size=128)

def fitting_detector(detector, train_loader, device):
    detector.fit(train_loader, device=device)


def make_detector(detector_name, model, train_loader, device):
    mean=[0.485, 0.456, 0.406]
    std=[0.229, 0.224, 0.225]
    if detector_name == 'MCD':
        detector = MCD(model)
    elif detector_name == 'TemperatureScaling':
        detector = TemperatureScaling(model)
    elif detector_name == 'OpenMax':
        detector = OpenMax(model)
    elif detector_name == 'KNN':
        detector = KNN(model)
    elif detector_name == 'ASH':
        detector = detector = ASH(backbone = model.features_before_pool, head = model.forward_from_before_pool, detector=EnergyBased.score)
    elif detector_name == 'ReAct':
        detector = ReAct(backbone = model.features, head = model.fc, detector = EnergyBased.score)
    elif detector_name == 'Entropy':
        detector = Entropy(model)
    elif detector_name == 'ViM':
        detector = ViM(model.features, d=64, w=model.fc.weight, b=model.fc.bias)
    elif detector_name == 'Mahalanobis+ODIN':
        detector = Mahalanobis(model.features, norm_std=std, eps=0.002)
    elif detector_name == 'Mahalanobis':
        detector = Mahalanobis(model.features)
    elif detector_name == 'KLMatching':
        detector = KLMatching(model)
    elif detector_name == 'SHE':
        detector = SHE(model.features, model.fc)
    elif detector_name == 'MSP':
        detector = MaxSoftmax(model)
    elif detector_name == 'EnergyBased':
        detector = EnergyBased(model)
    elif detector_name == 'MaxLogit':
        detector = MaxLogit(model)
    elif detector_name == 'ODIN':
        detector = ODIN(model, norm_std=std, eps=0.002)
    elif detector_name == 'DICE':
        detector = DICE(model=model.features, w=model.fc.weight, b=model.fc.bias, p=0.65)
    elif detector_name == 'RMD':
        detector = RMD(model.features)

    fitting_detector(detector, train_loader, device)
    return detector

if __name__ == '__main__':
    main()
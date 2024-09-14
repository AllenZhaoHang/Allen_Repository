

from pytorch_ood.model import WideResNet

def make_model(model_name=WideResNet, device='cuda:0'):

    if model_name == 'WideResNet':
        model = WideResNet(num_classes=10, pretrained="cifar10-pt").eval().to(device)


    return model
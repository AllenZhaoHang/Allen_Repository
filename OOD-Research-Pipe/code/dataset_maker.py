import torchvision.transforms as tvt
from torchvision.datasets import CIFAR10, CIFAR100, MNIST
from torch.utils.data import DataLoader
from pytorch_ood.utils import ToRGB

def make_dataset(dataset_name, batch_size=128):
    mean=[0.485, 0.456, 0.406]
    std=[0.229, 0.224, 0.225]
    trans = tvt.Compose([tvt.Resize(size=(32, 32)), ToRGB(), tvt.ToTensor(), tvt.Normalize(std=std, mean=mean)])
    root = './dataset'

    if dataset_name == 'cifar10':
        dataset_in_train = CIFAR10(root="data", train=True, transform=trans, download=True)
        dataset_in_test = CIFAR10(root="data", train=False, transform=trans, download=True)
    elif dataset_name == 'cifar100':
        dataset_in_train = CIFAR100(root="data", train=True, transform=trans, download=True)
        dataset_in_test = CIFAR100(root="data", train=False, transform=trans, download=True)
    elif dataset_name == 'mnist':
        dataset_in_train = CIFAR10(root="data", train=True, transform=trans, download=True)
        dataset_in_test = CIFAR10(root="data", train=False, transform=trans, download=True)

    train_loader = DataLoader(dataset_in_train, batch_size=batch_size)
    test_loader = DataLoader(dataset_in_test, batch_size=batch_size)

    return train_loader, test_loader






if __name__ == '__main__':
    main()

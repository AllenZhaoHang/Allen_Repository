import os
current_path = os.getcwd()  # 获取当前工作目录
folder_path = os.path.join(current_path, 'output', 'attacked_data')
if not os.path.exists(folder_path):
    os.makedirs(folder_path)



folder_path = os.path.join(current_path, 'output', 'detector_result')
if not os.path.exists(folder_path):
    os.makedirs(folder_path)





## download dataset
from torchvision.datasets import CIFAR10
import torchvision.transforms as tvt
mean=[0.485, 0.456, 0.406]
std=[0.229, 0.224, 0.225]
trans = tvt.Compose([tvt.Resize(size=(32, 32)), ToRGB(), tvt.ToTensor(), tvt.Normalize(std=std, mean=mean)])
dataset_in_train = CIFAR10(root="data", train=True, transform=trans, download=True)
dataset_in_test = CIFAR10(root="data", train=False, transform=trans, download=True)
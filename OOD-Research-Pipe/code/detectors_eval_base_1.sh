#!/bin/bash
python dir_prep.py
wait
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data PGD_cifar10 --detector ReAct &
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data PGD_cifar10 --detector OpenMax &
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data PGD_cifar10 --detector TemperatureScaling &
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data PGD_cifar10 --detector KNN 
wait
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data PGD_cifar10 --detector ODIN &
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data PGD_cifar10 --detector EnergyBased &
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data PGD_cifar10 --detector Entropy &
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data PGD_cifar10 --detector KLMatching 
wait
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data PGD_cifar10 --detector Mahalanobis &
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data PGD_cifar10 --detector Mahalanobis+ODIN &
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data PGD_cifar10 --detector MaxLogit &
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data PGD_cifar10 --detector ViM 
wait
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data PGD_cifar10 --detector RMD &
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data PGD_cifar10 --detector DICE &
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data PGD_cifar10 --detector SHE &
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data PGD_cifar10 --detector MSP 
wait
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data PGD_cifar10 --detector MCD &
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data PGD_cifar10 --detector ASH &
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data FGSM_cifar10 --detector ReAct &
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data FGSM_cifar10 --detector OpenMax 
wait
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data FGSM_cifar10 --detector TemperatureScaling &
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data FGSM_cifar10 --detector KNN &
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data FGSM_cifar10 --detector ODIN &
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data FGSM_cifar10 --detector EnergyBased 
wait
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data FGSM_cifar10 --detector Entropy &
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data FGSM_cifar10 --detector KLMatching &
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data FGSM_cifar10 --detector Mahalanobis &
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data FGSM_cifar10 --detector Mahalanobis+ODIN 
wait
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data FGSM_cifar10 --detector MaxLogit &
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data FGSM_cifar10 --detector ViM &
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data FGSM_cifar10 --detector RMD &
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data FGSM_cifar10 --detector DICE 
wait
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data FGSM_cifar10 --detector SHE &
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data FGSM_cifar10 --detector MSP &
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data FGSM_cifar10 --detector MCD &
CUDA_VISIBLE_DEVICES="0" python detectors_eval.py --model WideResNet --attack_data FGSM_cifar10 --detector ASH 
wait

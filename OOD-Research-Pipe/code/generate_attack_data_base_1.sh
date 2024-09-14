#!/bin/bash
python dir_prep.py
wait
CUDA_VISIBLE_DEVICES="0" python generate_attack_data.py --attack_name VANILA --dataset cifar10&
CUDA_VISIBLE_DEVICES="1" python generate_attack_data.py --attack_name GN --dataset cifar10&
CUDA_VISIBLE_DEVICES="2" python generate_attack_data.py --attack_name FGSM --dataset cifar10&
CUDA_VISIBLE_DEVICES="3" python generate_attack_data.py --attack_name BIM --dataset cifar10
wait
CUDA_VISIBLE_DEVICES="0" python generate_attack_data.py --attack_name RFGSM --dataset cifar10&
CUDA_VISIBLE_DEVICES="1" python generate_attack_data.py --attack_name PGD --dataset cifar10&
CUDA_VISIBLE_DEVICES="2" python generate_attack_data.py --attack_name EOTPGD --dataset cifar10&
CUDA_VISIBLE_DEVICES="3" python generate_attack_data.py --attack_name FFGSM --dataset cifar10
wait
CUDA_VISIBLE_DEVICES="0" python generate_attack_data.py --attack_name TPGD --dataset cifar10&
CUDA_VISIBLE_DEVICES="1" python generate_attack_data.py --attack_name MIFGSM --dataset cifar10&
CUDA_VISIBLE_DEVICES="2" python generate_attack_data.py --attack_name UPGD --dataset cifar10&
CUDA_VISIBLE_DEVICES="3" python generate_attack_data.py --attack_name APGD --dataset cifar10
wait
CUDA_VISIBLE_DEVICES="0" python generate_attack_data.py --attack_name APGDT --dataset cifar10&
CUDA_VISIBLE_DEVICES="1" python generate_attack_data.py --attack_name DIFGSM --dataset cifar10&
CUDA_VISIBLE_DEVICES="2" python generate_attack_data.py --attack_name TIFGSM --dataset cifar10&
CUDA_VISIBLE_DEVICES="3" python generate_attack_data.py --attack_name Jitter --dataset cifar10
wait
CUDA_VISIBLE_DEVICES="0" python generate_attack_data.py --attack_name NIFGSM --dataset cifar10&
CUDA_VISIBLE_DEVICES="1" python generate_attack_data.py --attack_name PGDRS --dataset cifar10&
CUDA_VISIBLE_DEVICES="2" python generate_attack_data.py --attack_name SINIFGSM --dataset cifar10&
CUDA_VISIBLE_DEVICES="3" python generate_attack_data.py --attack_name VMIFGSM --dataset cifar10
wait
CUDA_VISIBLE_DEVICES="0" python generate_attack_data.py --attack_name VNIFGSM --dataset cifar10&
CUDA_VISIBLE_DEVICES="1" python generate_attack_data.py --attack_name CW --dataset cifar10&
CUDA_VISIBLE_DEVICES="2" python generate_attack_data.py --attack_name PGDL2 --dataset cifar10&
CUDA_VISIBLE_DEVICES="3" python generate_attack_data.py --attack_name PGDRSL2 --dataset cifar10
wait
CUDA_VISIBLE_DEVICES="0" python generate_attack_data.py --attack_name DeepFool --dataset cifar10&
CUDA_VISIBLE_DEVICES="1" python generate_attack_data.py --attack_name SparseFool --dataset cifar10&
CUDA_VISIBLE_DEVICES="2" python generate_attack_data.py --attack_name OnePixel --dataset cifar10&
CUDA_VISIBLE_DEVICES="3" python generate_attack_data.py --attack_name Pixle --dataset cifar10
wait
CUDA_VISIBLE_DEVICES="0" python generate_attack_data.py --attack_name FAB --dataset cifar10&
CUDA_VISIBLE_DEVICES="1" python generate_attack_data.py --attack_name AutoAttack --dataset cifar10&
CUDA_VISIBLE_DEVICES="2" python generate_attack_data.py --attack_name Square --dataset cifar10&
CUDA_VISIBLE_DEVICES="3" python generate_attack_data.py --attack_name SPSA --dataset cifar10
wait
CUDA_VISIBLE_DEVICES="0" python generate_attack_data.py --attack_name JSMA --dataset cifar10&
CUDA_VISIBLE_DEVICES="1" python generate_attack_data.py --attack_name EADL1 --dataset cifar10&
CUDA_VISIBLE_DEVICES="2" python generate_attack_data.py --attack_name EADEN --dataset cifar10&
CUDA_VISIBLE_DEVICES="3" python generate_attack_data.py --attack_name PIFGSM --dataset cifar10
wait
CUDA_VISIBLE_DEVICES="0" python generate_attack_data.py --attack_name PIFGSMPP --dataset cifar10&
wait

#!/bin/bash
CUDA_VISIBLE_DEVICES="0" python generate_attack_data.py --attack_name SparseFool --dataset cifar10&
CUDA_VISIBLE_DEVICES="1" python generate_attack_data.py --attack_name JSMA --dataset cifar10
wait
CUDA_VISIBLE_DEVICES="0" python generate_attack_data.py --attack_name OnePixel --dataset cifar10&
CUDA_VISIBLE_DEVICES="1" python generate_attack_data.py --attack_name Square --dataset cifar10
wait
CUDA_VISIBLE_DEVICES="0" python generate_attack_data.py --attack_name DeepFool --dataset cifar10&
CUDA_VISIBLE_DEVICES="1" python generate_attack_data.py --attack_name Pixle --dataset cifar10
wait
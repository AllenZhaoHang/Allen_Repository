#!/bin/bash
#SBATCH --nodes=1
#SBATCH -p v100
#SBATCH --gres=gpu:v100:4
#SBATCH --mem=120g
#SBATCH --time=8:00:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=zhan8023@umn.edu
module load cuda/12.0
nvidia-smi
bash generate_attack_data_base_1.sh > result

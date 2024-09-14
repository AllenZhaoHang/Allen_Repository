#!/bin/bash -l
#sbatch --time=2:00:00
#sbatch --mem=10g
#sbatch --tmp=10g
#sbatch -mail-type=ALL
#sbatch --mail-user=zhan8023@umn.edu
#sbatch -p a100-4
#sbatch --gres=gpu:a100:1

cd ~/Desktop/MyPipe/
module load cuda/11.2
python generate_attack_data.py > result

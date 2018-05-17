#!/bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --time=100:00:00
#SBATCH --mem=40GB
#SBATCH --job-name=m-mozart
#SBATCH --mail-type=END
#SBATCH --mail-user=$USER@nyu.edu
#SBATCH --output=m_mozart.out
#SBATCH --gres=gpu:1

HOME=/home/$USER
DATA_DIR=/scratch/$USER/neural-editor-data
REPO_DIR=$HOME/neural-editor
export TEXTMORPH_DATA=$DATA_DIR

export PYTHONPATH=.:$REPO_DIR:$PYTHONPATH

/share/apps/singularity/2.5.1/bin/singularity exec --nv /beegfs/work/public/singularity/textmorph-1.2.img python $REPO_DIR/textmorph/edit_model/main.py $REPO_DIR/configs/edit_model/mono_mozart.txt

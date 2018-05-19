# Multi-modal Musical Phrase Completion

## MaskGAN Musical Phrase Completion
We use google cloud to train MaskGAN model.

### Setup Instructions

Please visit the original MaskGAN implementation [here](https://github.com/tensorflow/models/tree/master/research/maskgan).

In this project, we applied MaskGAN for Music Note.

**Addition Setup Notes**:


## Neural Editor Musical Phrase Completion
We use NYU's HPC Prince cluster to train our model.

### Setup Instructions

This model requires two folders: `neural-editor` and `neural-editor-data`. Both may be downloaded from current repo, in folder `neural-editor-model`.

For setup instructions to run locally, please visit the original [Neural Editor Setup instructions](https://github.com/kelvinguu/neural-editor/tree/readme).

**Additional Setup Notes**:
- `neural-editor-data` folder from Step 1 requires heavy memory storage, and should be saved to `/scratch/$USER/` for sufficient storage on NYU's HPC


### Create Training Run

After setup of `neural-editor` and `neural-editor-data`, training scripts for monophonic data are located in `neural-editor-model`. To run training on HPC, enter the following for the Bach dataset:

```
sbatch m_bach.s
```
To run other composers on simply replace the composer name: `sbatch m_<composer>.s` and submit.

**Additional Training Run Notes**:
- `sbatch` scripts run a Singularity image of Kelvin Guu's Docker image (kelvinguu/textmorph:1.2), already located on Prince's shared folders. 
- The training run will output a slurm file: `m_<dataset>.out`. This file will contain training loss information, as well as a few sample validation source and target outputs.


### Generating Output from Training Checkpoint

After training has completed, you can generate a Jupyer Notebook demo located inside of `neural-editor-model/neural-editor`. Once in `neural-editor-demo.ipynb` notebook, set `EDIT_RUN` to the desired composer. A map of existing training runs have been provided in the notebook.



## WavGAN Musical Phrase Completion

# Multi-modal Musical Phrase Completion

## MaskGAN Musical Phrase Completion
We use google cloud to train MaskGAN model.

### Setup Instructions

Please visit the original MaskGAN implementation [here](https://github.com/tensorflow/models/tree/master/research/maskgan).

In this project, we applied MaskGAN for Musical Phrase Completion.

'/tmp/data_dir' will have data set. <br/>
'/tmp/log_dir' will have model check points.<br/>

### Create Training Run
```bash
python train_mask_gan.py \
  --data_dir='/tmp/data_dir' \
  --batch_size=20 \
  --sequence_length=20 \
  --base_directory='/tmp/log_dir' \
  --mask_strategy=contiguous \
  --maskgan_ckpt= \
  --hparams="gen_rnn_size=64,dis_rnn_size=64,gen_num_layers=2,dis_num_layers=2,gen_learning_rate=0.00038877,gen_learning_rate_decay=1.0,gen_full_learning_rate_steps=120000,gen_vd_keep_prob=0.33971,rl_discount_rate=0.89072,dis_learning_rate=5e-4,baseline_decay=0.99,dis_train_iterations=2,dis_pretrain_learning_rate=0.005,critic_learning_rate=5.1761e-7,dis_vd_keep_prob=0.71940" --mode='TRAIN' --max_steps=30000 --generator_model='seq2seq_vd' --discriminator_model='seq2seq_vd' --is_present_rate=0.55 \
  --summaries_every=250 \
  --print_every=250 \
  --max_num_to_print=3 \
  --gen_training_strategy='reinforce' \
  --seq2seq_share_embedding=true \
  --baseline_method=critic \
  --attention_option=luong
```

We didn't pretrain the model for the Musical Phrase Completion.

### Generating Output from Training Checkpoint
```bash
python train_mask_gan.py \
  --data_dir='/tmp/data_dir' \
  --batch_size=20 \
  --sequence_length=20 \
  --base_directory='/tmp/log_dir' \
  --mask_strategy=contiguous \
  --maskgan_ckpt='/tmp/log_dir/train/model.ckpt-10000' \
  --hparams="gen_rnn_size=64,dis_rnn_size=64,gen_num_layers=2,dis_num_layers=2,gen_learning_rate=0.000038877,gen_learning_rate_decay=1.0,gen_full_learning_rate_steps=2000000,gen_vd_keep_prob=0.33971,rl_discount_rate=0.89072,dis_learning_rate=5e-4,baseline_decay=0.99,dis_train_iterations=2,dis_pretrain_learning_rate=0.005,critic_learning_rate=5.1761e-7,dis_vd_keep_prob=0.71940" \
  --mode='TEST' \
  --start_index=6 \
  --max_steps=10 \
  --generator_model='seq2seq_vd' \
  --discriminator_model='seq2seq_vd' \
  --is_present_rate=0.55 \
  --summaries_every=250 \
  --print_every=250 \
  --max_num_to_print=20 \
  --gen_training_strategy='reinforce' \
  --seq2seq_share_embedding=true \
  --baseline_method=critic \
  --attention_option=luong
```

We wanted to mask the notes from position 7 to 14 in the 20-note sequence for test, let model fill the missing notes.

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

# Explainable Musical Phrase Completion

This repository contains two models for musical phrase completion.

## Neural Editor Musical Phrase Completion

### Setup Instructions

This model requires two folders: `neural-editor` and `neural-editor-data`. Both may be downloaded from current repo, in folder `neural-editor-model`.

For setup instructions to run locally, please visit the original [Neural Editor Setup instructions](https://github.com/kelvinguu/neural-editor/tree/readme).

### Create Training Run

After setup of `neural-editor` and `neural-editor-data`, training scripts for monophonic data are located in `neural-editor-model`.


### Generating Output from Training Checkpoint

After training has completed, you can generate a Jupyter Notebook demo located inside of `neural-editor-model/neural-editor`. Once in `neural-editor-demo.ipynb` notebook, set `EDIT_RUN` to the desired composer. A map of existing training runs has been provided in the notebook.

## MaskGAN Musical Phrase Completion

### Setup Instructions

Please visit the original MaskGAN implementation [here](https://github.com/tensorflow/models/tree/master/research/maskgan).

'/tmp/data_dir' contains the data set. <br/>
'/tmp/log_dir' contains the model check points.<br/>

### Sample Create Training Run
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

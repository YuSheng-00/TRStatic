export MODEL_PATH="/root/model/llama3_8b/Meta-Llama-3-8B-Instruct"
export OUTPUT_PATH="./ckpts_new"
export MASTER_ADDR="localhost"
export WANDB_DISABLED=False
export NUM_GPUS=4

torchrun --master_addr ${MASTER_ADDR} \
  --nproc_per_node=${NUM_GPUS} \
  --master_port=6008 \
  tuning.py \
  --model_name_or_path $MODEL_PATH \
  --data_path "../datas/mixed_datas.json" \
  --bf16 True \
  --output_dir ${OUTPUT_PATH}\
  --num_train_epochs  3\
  --per_device_train_batch_size 2\
  --per_device_eval_batch_size 1 \
  --gradient_accumulation_steps 16 \
  --evaluation_strategy "no" \
  --save_strategy "steps" \
  --save_steps 300\
  --save_total_limit 1 \
  --learning_rate 5e-5 \
  --weight_decay 0.01 \
  --warmup_ratio 0.03 \
  --lr_scheduler_type "cosine" \
  --logging_steps 1 \
  --fsdp "full_shard auto_wrap" \
  --tf32 True \

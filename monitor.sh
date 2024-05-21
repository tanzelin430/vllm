#!/bin/bash

# 设置要监控的GPU ID
gpu_id=2

# 设置输出文件名
output_file="gpu_usage_log_gpu${gpu_id}.txt"

# 设置记录间隔时间（秒）
interval=1

# 写入文件头
echo "Date-Time, GPU${gpu_id} Utilization" > $output_file

# 开始循环记录
while true
do
    # 获取当前时间和指定GPU的利用率
    datetime=$(date '+%Y-%m-%d %H:%M:%S')
    gpu_util=$(nvidia-smi --id=$gpu_id --query-gpu=utilization.gpu --format=csv,noheader,nounits)

    # 输出到文件
    echo "$datetime, $gpu_util" >> $output_file

    # 等待一段时间
    sleep $interval
done
#!/bin/bash

# 输出文件
output_file="benchmark_results.txt"

# 如果输出文件已存在，则先删除
if [ -f "$output_file" ]; then
    rm "$output_file"
fi

# 开始值
start=384
# 结束值
end=3840
# 步长
step=128

# 循环从start到end，每次增加step
for (( value=$start; value<=$end; value+=step ))
do
  echo "Running benchmark with max-num-batched-tokens=$value" | tee -a "$output_file"
  # 将命令输出同时发送到stdout和文件
  python benchmark_throughput.py --enforce-eager --enable-chunked-prefill --max-num-batched-tokens=$value 2>&1 | tee -a "$output_file"
done
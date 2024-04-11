# 假设您的数据存储在一个名为data.txt的文件中
input_file = 'logstats.log'
output_file = 'processed_data.txt'

# 打开文件进行读写
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        # 分割每行数据以获取所需的部分
        parts = line.strip().split()
        time = parts[2]  # 时间信息在第二个位置
        action = 'prefill' if 'Prefilled' in line else 'generate'  # 根据行内容判断操作类型
        tokens = parts[-2]  # token数量在倒数第二个位置
        # 将处理后的数据写入新文件
        outfile.write(f"{time} {action} {tokens}\n")

print("处理完成。")
import matplotlib.pyplot as plt

# 文件路径
input_file = 'processed_data.txt'

# 初始化列表来存储generate操作的token数目
generate_tokens = []

# 从文件中读取数据
with open(input_file, 'r') as file:
    for line in file:
        _, action, token = line.strip().split()
        if action == 'generate':
            generate_tokens.append(int(token))

# 绘制直方图
plt.hist(generate_tokens, bins=20, color='red', alpha=0.7)

# 设置图表标题和坐标轴标签
plt.title('Distribution of Generate Tokens')
plt.xlabel('Number of Tokens')
plt.ylabel('Frequency')

# 显示图表
plt.show()
plt.savefig('generate_tokens_histogram.png')
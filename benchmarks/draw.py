import matplotlib.pyplot as plt

# 读取数据
with open('e2ere.txt', 'r') as file:
    lines = file.readlines()
    data = [float(line.strip()) for line in lines]

# 数据处理
data[0] = 1/data[0]
for i in range(1, len(data)):
    data[i] = ((i) * 8) / data[i]

# 生成横坐标
x = [1] + list(range(8, (len(data)) * 8, 8))

# 绘图
plt.figure(figsize=(10, 6))  # 设置图形的大小
plt.plot(x, data, marker='o', label='All Points')  # 使用圆圈标记每个数据点

# 着重展示横坐标是128的倍数的数据点
highlight_x = [xi for xi in x if xi % 128 == 0]
highlight_y = [data[x.index(xi)] for xi in highlight_x]

max_value = max(data)
max_index = data.index(max_value)
plt.annotate(f'Max: ({x[max_index]}, {max_value:.2f})',  # 显示坐标，保留两位小数
             (x[max_index], max_value),
             textcoords="offset points",  # 相对于点的位置
             xytext=(0,10),  # 文本的偏移量
             ha='center')  # 水平居中

plt.scatter(highlight_x, highlight_y, color='red', s=100, label='Multiples of 128', zorder=5)  # 使用红色标记，zorder确保这些点在最上层

plt.title('Data from e2eresult.txt')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)  # 显示网格
plt.legend()  # 显示图例
plt.savefig('e2eresultwithI8_highlighted.png')  # 保存图片
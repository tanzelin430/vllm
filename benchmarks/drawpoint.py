import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# 文件路径
input_file = 'processed_data.txt'

# 初始化列表来存储时间、token数目和颜色
times = []
tokens = []
colors = []

# 从文件中读取数据
with open(input_file, 'r') as file:
    for line in file:
        time_str, action, token = line.strip().split()
        # 将时间字符串转换为datetime对象
        time = datetime.strptime(time_str, '%H:%M:%S')
        times.append(time)
        tokens.append(int(token))
        if action == 'prefill':
            colors.append('blue')  # prefill操作用蓝色表示
        else:
            colors.append('red')  # generate操作用红色表示

# 创建图表和坐标轴
fig, ax = plt.subplots()

# 绘制点状图
ax.scatter(times, tokens, c=colors)

# 设置图表标题和坐标轴标签
ax.set_title('Token Operations Over Time')
ax.set_xlabel('Time')
ax.set_ylabel('Number of Tokens')

# 设置x轴以显示时间
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=1))  # 每1分钟显示一个刻度
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))  # 时间格式

# 自动格式化x轴上的日期显示（倾斜等）
fig.autofmt_xdate()

plt.show()
plt.savefig('token_operations.png')
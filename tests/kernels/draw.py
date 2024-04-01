import csv
import matplotlib.pyplot as plt
# 从命令行接受参数
import sys
filename = sys.argv[1]
num_of_reqs = int(sys.argv[2])
# 读取CSV文件并删除每个数据开头的'.'
with open(f'{filename}', 'r') as file:
    reader = csv.reader(file, delimiter=' ')
    data = [[float(row[0][1:]), int(row[1]), int(row[2])] for row in reader]

# 按照请求数量和计算资源数量对数据进行排序
data.sort(key=lambda x: (x[1], x[2]))

# 将数据按照请求数量进行分类
data_by_requests = {}
for row in data:
    if row[1] not in data_by_requests:
        data_by_requests[row[1]] = []
    data_by_requests[row[1]].append(row)

# 筛选request数量为100的数据
request_100_data = data_by_requests[num_of_reqs]

# 绘制图形
x = [row[2] for row in request_100_data]
y = [row[0] for row in request_100_data]  # 转换为微秒
plt.plot(x, y, marker='o', linestyle='-', label=f'{num_of_reqs} requests')

plt.xlabel('Number of Computing Resources')
plt.ylabel('Running Time (microseconds)')
plt.legend()
plt.show()
#save
plt.savefig(f'{filename}.png')
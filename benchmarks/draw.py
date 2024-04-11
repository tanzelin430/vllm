import matplotlib.pyplot as plt

# 从 prefill.log 文件中读取数据
with open("prefill2.log", "r") as f:
    data = [float(line.strip()) for line in f.readlines()]

# 创建横坐标（batch_size）
batch_sizes = list(range(1, len(data) + 1))

for i in range(len(batch_sizes)):
    batch_sizes[i] = batch_sizes[i] * 10
# 绘制图形
plt.plot(batch_sizes, data)
plt.xlabel("token")
plt.ylabel("Latency (seconds)")
plt.title("prefill latency with tokens")
plt.grid()

# 显示图形
plt.show()

plt.savefig("prefill2.png")

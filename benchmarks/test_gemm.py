import torch
import time
from tqdm import tqdm
hidden_size = 4096

# 设置一个batch_size列表，用于测试不同的batch_size
# batch_sizes = [1, 10, 100, 500, 1000, 5000, 10000]

# 用于存储每个batch_size的计算时间
times = []
batch_sizes = range(1, 2000)
# 对于每个batch_size，执行矩阵乘法并记录时间
for batch_size in tqdm(batch_sizes, desc='test_gemm'):
    # 创建两个随机矩阵，大小分别为[batch_size, hidden_size]和[hidden_size, hidden_size]
    mat1 = torch.randn(batch_size, hidden_size).cuda()
    mat2 = torch.randn(hidden_size, hidden_size).cuda()
    # warm up
    for _ in range(10):
        result = torch.matmul(mat1, mat2)
    torch.cuda.synchronize()
    # 记录开始时间
    start_time = time.time()

    # 执行矩阵乘法
    for _ in range(10):
        result = torch.matmul(mat1, mat2)
    # 记录结束时间
    torch.cuda.synchronize()
    end_time = time.time()

    # 计算并存储执行时间
    elapsed_time = end_time - start_time
    times.append(elapsed_time/10)

    # print(f"Batch size: {batch_size}, Time: {elapsed_time:.6f} seconds")

# 绘制batch_size与计算时间的关系图
import matplotlib.pyplot as plt

plt.plot(batch_sizes, times, marker='o')
plt.xlabel("tokens")
plt.ylabel("Time (seconds)")
plt.title("Time vs Batch size for matrix multiplication")
plt.grid()
plt.show()
plt.savefig('test_gemm.png')
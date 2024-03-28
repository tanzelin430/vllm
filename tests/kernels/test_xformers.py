import torch
import xformers.ops as xops


B, M, K = 3, 32, 128
kwargs = dict(device="cuda", dtype=torch.float32)
q = torch.randn([B, M, 8, K], **kwargs)
k = torch.randn([B, M, 2, K], **kwargs)
v = torch.randn([B, M, 2, K], **kwargs)
out_gqa = xops.memory_efficient_attention_forward(
    q.reshape([B, M, 2, 4, K]),
    k.reshape([B, M, 2, 1, K]).expand([B, M, 2, 4, K]),
    v.reshape([B, M, 2, 1, K]).expand([B, M, 2, 4, K]),
)

import torch
# create two tensor based on list
a = torch.tensor([1, 2, 3, 4, 5,7,8,9])
b = torch.tensor([6, 7, 8, 9, 10])



# concat a and b
a_b = torch.cat([a, b],dim=0)
print(a_b)

a,b = torch.split(a_b, [len(a), len(b)])
print(a)
print(b)
import numpy as np
import torch
import random

# a = np.arange(6)
# print(a)
# print(a[0:6])
#
# b = [5, 6, 4]
# print(b[0:2])

# print(random.randint(0, 200))
# a = torch.tensor([[random.randint(0, 200)]])
# print(a)
a = torch.Tensor([0.5, 0.1, 0, 0.00000001, -1000000, -0.00000001])
b = torch.softmax(a, 0)
print(b)

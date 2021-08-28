"""How is Pytorch’s binary_cross_entropy_with_logits function related to sigmoid and binary_cross_entropy

This notebook breaks down how binary_cross_entropy_with_logits function (corresponding to BCEWithLogitsLoss used for multilabel classification)
is implemented in pytorch, and how it is related to sigmoid and binary_cross_entropy
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

def sigmoid(x): return (1 + (-x).exp()).reciprocal()
def binary_cross_entropy(pred, y): return -(pred.log()*y + (1-y)*(1-pred).log()).mean()

batch_size, n_classes = 10, 4
# Features
x = torch.randn(batch_size, n_classes)
print(x)
# Target
target = torch.randint(n_classes, size=(batch_size,), dtype=torch.long)
print(target)
# One Hot Target
y = torch.zeros(batch_size, n_classes)
y[range(y.shape[0]), target]=1
print(y)

# sigmoid + binary_cross_entropy
pred = sigmoid(x)
loss = binary_cross_entropy(pred, y)
print(loss) # tensor(0.8630)

# F.sigmoid + F.binary_cross_entropy
pred = F.sigmoid(x)
loss = F.binary_cross_entropy(pred, y)
print(loss)  # tensor(0.8630)

# F.binary_cross_entropy_with_logits
print(F.binary_cross_entropy_with_logits(x, y)) # tensor(0.8630)

# Both will give Same Loss
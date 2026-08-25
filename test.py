import numpy as np
dW = np.array([[1,2,3,4],[2,3,6,7]])
W = np.cumsum(dW,axis=1)
Wmean = np.mean(W,axis=1)
print(W)
print(Wmean)

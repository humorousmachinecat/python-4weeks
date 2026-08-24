#追加元素
import numpy as np
x = np.array([6,9,1])
x = np.append(x,values=4)
print(x)
#删除元素
x = np.delete(x,2)
print(x)

#生成 10000 个标准正态随机数，算均值/方差。
# np.random.seed(10)
# arr1 = np.random.randn(10000)
# print(np.mean(arr1))
# print(np.mean((arr1-np.mean(arr1))**2))
# print(np.var(arr1))

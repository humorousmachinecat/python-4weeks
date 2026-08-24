import numpy as np

#追加元素
x = np.array([6,9,1])
x = np.append(x,4)
print(x)

#删除元素
x = np.delete(x,2)      #删除x[2]这个数据 x = np.delete(删除的ndarray，索引)
print(x)
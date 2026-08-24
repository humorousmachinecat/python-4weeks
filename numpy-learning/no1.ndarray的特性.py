#ndarray
#1.ndarray的特性
##多维性
import numpy as np
arr1 = np.array([[1,2,5],[0,2,4],[0,4,5]])
arr2 = np.array(1)
arr3 = np.array([1,2])
print('arr1 =',arr1)
print('arr2 =',arr2)
print('arr3 =',arr3)
print('the dimensions of arr1 is',arr1.ndim)
print('the dimensions of arr2 is',arr2.ndim)
print('the dimensions of arr3 is',arr3.ndim)

##同质性
arr4 = np.array([1,'hello'])
print('arr4 =',arr4)     #不同的数据类型会被强制转换成相同的数据类型
arr5 = np.array([1,2.5,3.005])
print('arr 5 =',arr5)     #1转换成浮点型

##高效性：基于连续内存块存储，支持向量化运算
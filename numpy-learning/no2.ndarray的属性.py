import numpy as np
arr1 = np.array(1.0)
arr2 = np.array(['hello','world','i\'m','humoct'])
arr3 = np.array([[1,1],[1,2],[1,1]])
print('arr1 =',arr1)
print('arr2 =',arr2)
print('arr3 =\n',arr3)
#ndim	数组的秩，即数组的维度数量或轴的数量。跟矩阵的秩不同。
print('every array\'s ndim      数组的秩，数组的维度')
print('arr1.ndim =',arr1.ndim)
print('arr2.ndim =',arr2.ndim)
print('arr3.ndim =',arr3.ndim)
#shape	表示数组在每个轴上的大小。对于二维数组（矩阵），表示其行数和列数。
print('every array\'s shape     表示数组在每个轴上的大小。对于二维数组（矩阵），表示其行数和列数。')
print('arr1.shape =',arr1.shape)    #0维不显示shape
print('arr2.shape =',arr2.shape)    #1维显示（3，）
print('arr3.shape =',arr3.shape)
#size	数组中元素的总个数，等于 ndarray.shape 中各个轴上大小的乘积。
print('every array\'s size      数组中元素的总个数')
print('arr1.size =',arr1.size) 
print('arr2.size =',arr2.size)    
print('arr3.size =',arr3.size)
#dtype	数组中元素的数据类型。
print('every array\'s dtype     数组中元素的数据类型')
print('arr1.dtype =',arr1.dtype) 
print('arr2.dtype =',arr2.dtype)    
print('arr3.dtype =',arr3.dtype)
#T      数组的转置。
print('every array\'s T         数组的转置')
print('arr1.T =',arr1.T) 
print('arr2.T =',arr2.T)    
print('arr3.T =\n',arr3.T)
#itemsize	数组中每个元素的大小，以字节为单位。
print('every array\'s itemsiez  数组中每个元素的大小，以字节为单位')
print('arr1.itemsize =',arr1.itemsize) 
print('arr2.itemsize =',arr2.itemsize)    
print('arr3.itemsize =',arr3.itemsize)
#flags	包含有关内存布局的信息，如是否为 C 或 Fortran 连续存储，是否为只读等。
#real	数组中每个元素的实部（如果元素类型为复数）。
#imag	数组中每个元素的虚部（如果元素类型为复数）。
#data	实际存储数组元素的缓冲区，一般通过索引访问元素，不直接使用该属性。


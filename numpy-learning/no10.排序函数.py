import numpy as np

#排序函数
np.random.seed(10)
arr1 = np.random.randint(1,100,20)
arr2 = np.random.randint(1,100,20)
print(arr1)
arr1.sort()                                         #改变了arr这个原始的数组的排序,只能排序整数
print(arr1)
print('arr2 = \n',arr2)
print('改变排序后 arr2 = \n',np.sort(arr2))          #不改变原始数组
print('检验arr2原始数据是否改变 arr2 = \n',arr2)
#查看排序索引
print('排序索引为\n',np.argsort(arr2))

#去重函数
print(np.unique(arr2))                              #去重的同时会进行排序

#两个数组的拼接
print(np.concatenate((arr1,arr2)))

#数组的分割
print(np.split(arr2,5))                             #数组的长度要被5给整除，才能刚好分成5份
print(np.split(arr2,[6,12,18]))                     #分成6，6，6，2的数组

#调整数组形状
print(np.reshape(arr2,[2,10]))                      #也要刚好被分成2行10列这种形式
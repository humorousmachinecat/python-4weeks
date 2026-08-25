import numpy as np

#追加元素
x = np.array([6,9,1])
x = np.append(x,4)
print(x)

#删除元素
x = np.delete(x,2)      
#删除x[2]这个数据 x = np.delete(删除的ndarray，索引)
print(x)

#插入元素
y = [1,2,3]
x = np.insert(x,0,y,axis=0)
#np.insert(原本的数组,位置，添加的数组，axis=0/1)
print(x)

arr1 = ([[1,2],[3,4],[5,6]])
arr2 = ([1,2,3])
arr1 = np.insert(arr1,[0],arr2,axis=1)
#位置[0]和位置0差别很大，注意区分
print(arr1)

arr1 = ([[1,2],[3,4],[5,6]])
arr1 = np.insert(arr1,0,arr2,axis=1)
print(arr1)
#插入数组时记得要同shape

#除了插入一个数组以外，还可以插入一个数
arr1 = ([[1,2],[3,4],[5,6]])
arr1 = np.insert(arr1,1,0,axis=1)
print(arr1)

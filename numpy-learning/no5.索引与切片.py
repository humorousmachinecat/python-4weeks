import numpy as np
np.random.seed(10)
arr1 = np.random.randint(1,100,20)
arr2 = np.random.randint(1,100,(4,5))
print(arr1)
print(arr2)
print('\nthe following is the exmple')
#基本索引:通过整数索引直接访问元素。索引从0开始。	
print('\n')
print(arr1[0])
print(arr2[1,3])

#行/列切片:使用冒号: 切片语法选择行或列的子集。	
print('\n')
print(arr1[:])                          #只有冒号就默认取第1行，对于1维数组即为整个数组
print(arr1[0:3])                        #切片的区间是左闭右开的区间，arr1[0,3]指 0≤x<3 这个范围，取第0，1，2个元素	
print(arr2[:,:])                        #输出整个2维数组
print(arr2[1,:])                        #取第1行所有
print(arr2[0,0:3])                      #取第0行第0，1，2元素

#slice 函数 :通过 slice(start, stop, step) 定义切片规则。
print('\n')	
print(arr1[slice(0,3)])                 #与arr1[0:3]等价
print(arr1[slice(2,15,3)])              #(start,end,step)

#布尔索引:通过布尔条件筛选满足条件的元素。支持逻辑运算符 &、|
print('\n')
print(arr1[(arr1>10) & (arr1<70)])      #bool索引，在数组中筛选出满足条件的
print(arr2[arr2>50])                    #针对2维数组应用bool索引，输出是1维数组，输出顺序从上到下，从左到右
print(arr2[0][arr2[0]>50])              #过滤出第0行的数据中大于50的部分
print(arr2[:,3][arr2[:,3]>50])          #过滤出第3列的数据中大于50的部分

#连续切片:从起始索引到结束索引按步长切片。

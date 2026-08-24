import numpy as np

#求和   计算平均值  计算中位数  标准差  方差
#最大值 最小值      计算分位数  累计和  累绩差

np.random.seed(20)
arr1 = np.random.randint(1,20,10)
print(arr1)

##求和
print(np.sum(arr1))

##计算平均值
print(np.average(arr1))
print(np.mean(arr1))

##计算中位数
print(np.median(arr1))

##计算方差和标准差
print(np.var(arr1))                     #方差
print(np.std(arr1))                     #标准差

##计算最大值，最小值
print(np.max(arr1),np.argmax(arr1))     #argmax(arr1)指的是arr1中最大值所在的位置
print(np.min(arr1),np.argmin(arr1))

##计算分位数
print(np.percentile(arr1,10))

##计算累计和，计算累计积
print(np.cumsum(arr1))                  #累计和
print(np.cumprod(arr1))                 #累计积
arr2 = np.array(range(1,11))
print(np.cumprod(arr2))                 #计算阶乘
import numpy as np

arr1 = np.array([[1,4,9],[1,4,9],[4,9,16]])
#生成均值为2，方差为9的样本
arr2 = np.random.normal(loc=2,scale=3,size=10000)

#基本数学函数

##计算平方根
print(np.sqrt(9))
print(np.sqrt(arr1))

##计算指数 e^x = y
print(np.exp(0))
print(np.exp(arr1))                 #以e为底的指数

##计算自然对数  lnx = y
print(np.log(2.71))                 #以e为底的对数

##计算正余弦值
print(np.sin(-1))
print(np.cos(np.pi))

##计算绝对值
arr3 = np.array([[-1,-2,3],[1,-1,2]])
print(np.abs(arr3))

##计算a的b次幂
print(np.power(arr3,2))

##四舍五入
print(np.round([3.2,4.5,5.5,9.6]))  #当小数部分为0.5时，向最近的偶数舍入。4.5-->4.0 ; 5.5-->6.0

##向上取整，向下取整
arr4 = np.array([1.6,2.3,4.5])
print(np.ceil(arr4))                #向上取整
print(np.floor(arr4))               #向下取整

#检测缺失值NaN
print(np.isnan([1,2,3]))
print(np.isnan([1,2,np.nan,3]))
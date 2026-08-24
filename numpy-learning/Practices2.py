# 题目5：数组变形
# 创造一个1到12的一维数组，并转行成（3，4）的二维数组
# -计算每行的和与每列的平均值
# -将数组展平为一维数组

import numpy as np
arr1 = np.array(range(1,13))
# arr1 = np.arange(1,13)
print(arr1)
arr1 = np.reshape(arr1,(3,4))
print(arr1)

# 计算每列的平均值与每行的和
print('every rows\' average = ',np.average(arr1,axis=0))        #每列的平均值
print('every lines\' sum = ',np.sum(arr1,axis=1))               #每行的和

# 将数组展平为一维数组
arr1 = np.reshape(arr1,12)          
# reshape(arr1,(m,n))化成(m，n)形状的矩阵  
# reshape(arr1,12)化成1行12列的一维数组
# arr1 = np.reshape(arr1,(12))                 
print(arr1)
print(np.ndim(arr1))



# 题目6：布尔索引
# 生成一个（5，5）的随机数组，范围[0，20]
# -找出所有大于10的元素
# -将所有大于10的元素替换为0

np.random.seed(10)
arr2 = np.random.randint(0,20,(5,5))
print(arr2)
print(arr2[arr2>10])
print(np.where(arr2>10,0,arr2))



# 题目7：统计函数的应用
# 某公司6个月的销售额（万元）为[120,135,110,125,130,140]
# -计算销售额的总和，均值和方差
# -找出销售额最高的月份和最低的月份

money = np.array([120,135,110,125,130,140])
print(np.sum(money),np.mean(money),np.var(money))
print(np.argmax(money)+1,np.argmin(money)+1)



# 题目8：数组拼接
# 给定A = [1,2,3] 和 B = [4，5，6]
# -将A和B水平拼接成一个新数组
# -将A和B垂直拼接成一个新数组

A = np.array([1,2,3])
B = np.array([4,5,6])
print(np.concatenate((A,B)))
print(np.reshape(np.concatenate((A,B)),(2,3)))



# 题目9：唯一值与排序
# 给定数组[2，1，2，3，1，4，3]
# -找出数组中的唯一值并排序
# -计算每个唯一值出现的次数

arr3 = np.array([2,1,2,3,1,4,3])
u_arr,counts = np.unique(arr3,return_counts=True)
#设置返回值为每个唯一值出现的次数
#u_arr,counts = np.unique(在arr3中的唯一值,返回次数=True)

print(u_arr)
print(counts)
print('\n')


# 题目10：综合运用
# 某商店5天的销售额和成本如下
# 销售额：[20,25,22,30,28]
# 成本：[15,18,16,22,20]
# -计算每天的利润
# -计算出利润的平均值和标准差
# -找出利润最高的天数

sell = np.array([20,25,22,30,28])
cost = np.array([15,18,16,22,20])
profit = sell-cost
print(profit)
print(np.mean(profit),np.std(profit))
print(len(profit[profit == np.max(profit)]))
# 题目1：温度数据分析
# 某城市一周的最高气温为[28,30,29,31,32,30,29]
# -计算平均气温，最高气温和最低气温。
# -找出气温超过30度的天数

import numpy as np
temps = np.array([28,30,29,31,32,30,29])

#平均气温，最高温，最低温
print('%.3f'%np.mean(temps))                #(%.3f%np.mean(temps)保留三位小数
print(np.max(temps))
print(np.min(temps))

#气温超过30度的天数
y=0
for x in temps:
    if x>30:
        y=y+1
print(y)

print(len(temps[temps>30]))                 #通过布尔索引筛选，再利用长度             
print(np.cumsum(np.where(temps>30,1,0))[-1])    
#通过np.where把大于30度的返回成1，然后利用cumsum计算和，最后取[-1]处的值
print(np.count_nonzero(temps>30))
print('\n')



# 题目2：学生成绩统计
# 某班级5名学生的数学成绩为[85,90,78,92,88].
# -计算平均分，中位数和标准差
# -将成绩转换为十分制度（假设满分为10）

#平均分，中位数和标准差
score = np.array([85,90,78,92,88])
print('average =',np.mean(score))
print('median =',np.median(score))
print('std =%.3f'%np.std(score))

#十分制
print(score/10)
print('\n')


 
# 题目3：矩阵运算
# 给定矩阵A=[[1,2],[3,4]]和B=[[5,6],[7,8]]
# -计算A + B 和 A * B
# -计算A和B的矩阵乘法

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(A+B)
print(A*B)
print(A@B)
print('\n')



# 题目4：随机数据生成
# 生成一个（3，4）的随机整数数组，范围[0，10)
# -计算每列的最大值和每行的最小值
# -将数组中的奇数替换成-1

#计算每列的最大值和每行的最小值
np.random.seed(20)
arr1 = np.random.randint(0,10,(3,4))
print(arr1)
# for x in range(0,4):
#     print(np.max(arr1[:,x]))
# for x in range(0,3):
#     print(np.max(arr1[x,:]))

print(np.max(arr1,axis=0))              #axis=0 列  =1 行
print(np.min(arr1,axis=1))

#将数组的所有奇数替换成-1
print(np.where(arr1 % 2 == 0,arr1,-1))


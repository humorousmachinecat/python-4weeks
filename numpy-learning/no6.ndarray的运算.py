import numpy as np
#数组与数组的计算
print('\n')
a = np.array([5,6,7])
b = np.array([1,2,4])
print(a+b)
print(a-b)
print(a*b)
print(a/b)                      #会自动输出成浮点型
print('\n')
ab = np.array(a/b, dtype=int)   #将浮点型截断成整型
print(ab)

#数组与标量的计算
c = np.array([[1,2],[3,4],[5,6]])
print('\n')
print(c+3)
print(c*3)
print(c/2)
print(c**2)

#矩阵的转置
print(c.T)

#broadcast机制
print('\n')                    
d = np.array([[1],[2],[3]])     #不同shape的数组，会补充成相同形状。必须是1行n列，n行1列使用broadcast
print(c+d)                      #broadcast只对一维数组生效
#[1,2]      [1]     [1,2]       [1,1]       [2,3]
#[3,4]  +   [2] =   [3,4]   +   [2,2]   =   [5,6]
#[5,6]      [3]     [5,6]       [3,3]       [8,9]

#矩阵运算
print('\n')
e = np.array([[1,2,3],[0,1,0],[0,0,1]])
f = np.array([[1,2,3],[4,5,6],[0,0,1]])
print(e@f)





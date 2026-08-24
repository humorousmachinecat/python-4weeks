import numpy as np
#基础构造：适用于手动构建小规模数组或复制已有数据
arr1 = np.array([[1,2],[2,3]])
print('arr1 =\n',arr1)

list1 =[4,5,6]
list2 =[1,1,1]
arr2 = np.array(list1)
arr3 = np.array([list1,list2])
print('arr2 =\n',arr2)
print('arr3 =\n',arr3)

arr4 = np.array(list1,dtype=np.float64)
print('arr4 =\n',arr4)

arr5 = np.copy(arr1)
print('arr5 copy arr1 =\n',arr5)                    #元素跟原始数组相同，但不是一个数组，指向不同地址
arr5[0][0] = 8
print('change arr5\'s the first element\n',arr5)

#预定义形状填充：用于快速初始化固定形状的数组，如全0占位、全1初始化。
prearr1 = np.zeros((3,2))                           #全0数组，（3，2）表示3行2列
print('prearr1 =\n',prearr1)

prearr2 = np.zeros((3,),dtype=int)                  #一维数组，dtype确定数据类型
print('prearr2 =',prearr2)

prearr3 = np.ones((3,3),dtype=int)                  #全1数组
print('prearr3 =\n',prearr3)

prearr4 = np.empty((2,2))                           #未初始化，可以不指定dtype
print('prearr4 =\n',prearr4)

prearr5 = np.full((2,2),2025,dtype=int)             #除0，1以外填满
print('prearr5 =\n',prearr5)

prearr6 = np.zeros_like(prearr5)                    #形状和元素数据类型prearr5一样的全0数组
print('prearr6 =\n',prearr6)                        #ones,empty，full也有类似指令
prearr7 = np.full_like(prearr5,2026)
print('prearr7 =\n',prearr7)                        #(形状，（数值），元素数据类型（dtype）)

#基于取值范围生成：生成数值序列，常用于模拟时间序列、坐标网格等。
rangearr1 = np.arange(4,10,2)                       #类似于等差数列,(start,end,step),取不到end
print('rangearr1 =\n',rangearr1)

rangearr2 = np.linspace(0,100,5,dtype=int)          #把0-100分成5份(start,end,num)，相当于（num-1）分点，此例中是4分点
print('rangearr2 =\n',rangearr2)

rangearr3 = np.logspace(0,4,3,base=3,dtype=int)     #(start,end,num,base=),先计算np.linspace(0,4,2),这里是[0,2,4]，然后再用base=3，有[3^0,3^2,3^4]
print('rangearr3 =\n',rangearr3)                    #不写base默认base = 10

#特殊矩阵生成：创建数学运算专用矩阵，例如线性代数中的单位矩阵。
spiarr1 = np.eye(3,4,dtype=int)                     #对角线全为1，可以通过(3,4,dtype=int)构造3行4列的对角线全为1的矩阵
print('spiarr1 =\n',spiarr1)

spiarr2 = np.diag([1,2,3])                          #对角矩阵，中间list填写的是对角元                          
print('spiarr2 =\n',spiarr2)

#随机数组生成：适用于模拟实验数据、初始化神经网络权重等场景。
randarr1 = np.random.rand(2,3)                      #生成0，1之间的随机浮点数（均匀分布，每个事件发生概率一样）
print('randarr1 =\n',randarr1)

randarr2 = np.random.uniform(3,6,(2,3))             #生成指定范围之间的随机浮点数
print('randarr2 =\n',randarr2)

randarr3 = np.random.randint(3,30,(2,3))            #生成指定范围之间的随机整数
print('randarr3 =\n',randarr3)

randarr4 = np.random.randn(2,3)                     #生成正态分布的随机浮点数
print('randarr4 =\n',randarr4)

np.random.seed(20)                                  #类似于我的世界输入的随机种子，保证每个人生成的随机数是相同的
randarr5 = np.random.randint(1,10,(2,5))
print('randarr5 =\n',randarr5)

#高级构造方法：用于处理非结构化数据，如文件、字符串，或通过函数生成复杂数组。

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams     
rcParams['font.family'] = 'SimHei'

n = 100000
np.random.seed(10)
sample = np.random.randint(0,7,(n,30))
average = np.round(np.average(sample, axis=1), 2)
unique,counts = np.unique(average,return_counts=True)
print(unique)
print(counts)

plt.figure(figsize=(10,5))
plt.bar(unique,counts,
        width=0.02,
        label ='均值')

plt.xticks(unique,rotation = 45,fontsize = 6)       
# 强制刻度等于 unique（仅当值很少时）

plt.tight_layout()


# m = len(unique)
# plt.hist(average,
#          bins=m,
#          rwidth=0.9)          
# #在这里这个数据不够连续，
# #把sample = np.random.randint(0,7,(n,L))中的L取长一点时，可以近似看作连续


# #  plt.hist(
# #       data,
# #       bins=30,            # 分箱数
# #       range=(-3, 3),      # 只统计这个范围内的数据
# #       density=True,       # True：显示概率密度（面积=1），而不是次数
# #       alpha=0.7,          # 透明度 0~1
# #       color='steelblue',  # 颜色
# #       edgecolor='black',  # 柱子描边颜色
# #       rwidth=0.9,         # 柱子占箱宽的相对比例，<1 时柱子间有空隙
# #   )
# # plt.hist 会返回三个东西，有时有用：
# #   n, bins, patches = plt.hist(data, bins=20)
# #   print(n)      # 每个箱子里有多少个数
# #   print(bins)   # 每个箱子的边界
# # plt.hist 用来看连续数据的分布，适用于均值，身高，成绩等连续值


plt.show()
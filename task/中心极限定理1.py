import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams     
rcParams['font.family'] = 'SimHei'

sample = []
average = []
# np.random.seed(10)
m = 1000000
for i in range(m):
    sample.append(np.random.randint(0,7,30))
for i in range(m):
    average.append('%.2f'%np.mean(sample[i]))

sa = np.array(sample)
aver = np.array(average)

unique = np.unique(aver)
aver.sort()
# print(unique)
# print(aver)
n = len(unique)
counts = []

for i in range(n):
    counts.append(len(aver[aver == unique[i]]))
#问题出在 average 是一个 Python 列表（list），而不是 numpy 数组
# 根本原因
# 看这一行：
# counts.append(len(average[average == unique[i]]))
# average 是列表，unique[i] 是字符串。当列表和一个字符串比较时：
# average == unique[i]   # 一个列表 == 一个字符串 → 结果是 False（不是逐元素比较！）
# 所以：
# average[False]   # False 相当于 0 → 取列表第 0 个元素，也就是一个字符串，比如 "3.27"
# len(average[False])   # len("3.27") = 4



plt.figure(figsize=(10,5))
plt.bar(unique,counts,
        label ='均值')
plt.xticks(rotation = 45,fontsize = 6)
plt.tight_layout()
plt.show()



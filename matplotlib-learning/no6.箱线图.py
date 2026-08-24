import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib import rcParams     
rcParams['font.family'] = 'SimHei'

#创造图表，设置大小
plt.figure(figsize=(8,6))
#plt.figure(figsize=(宽度,高度)) 

data = {
    '语文':[82,85,88,70,90,54,54,83,95],
    '数学':[70,65,45,76,85,74,60,86,67],
    '英语':[88,67,75,87,56,76,87,67,56]
}

plt.boxplot(data.values(),tick_labels=data.keys())

plt.title('各科成绩')

plt.grid(True,axis='y',linestyle='--',alpha=0.5)

plt.show()
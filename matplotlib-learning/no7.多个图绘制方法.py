import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib import rcParams     
rcParams['font.family'] = 'SimHei'

#设置折线图数据
month = ['1','2','3','4']
sales = [100,50,77,56]

f1 = plt.subplot(2,2,1)         #plt.subplot(一共几行，一共几列，排第几个)
f1.plot(month,sales)
f2 = plt.subplot(2,2,2)
f2.bar(month,sales)
f3 = plt.subplot(2,2,3)
f3.scatter(month,sales)
plt.show()
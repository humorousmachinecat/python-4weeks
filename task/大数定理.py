import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams     
rcParams['font.family'] = 'SimHei'

colors = ['#66b3ff','#99ff99','#ffcc99','#ff9999','#ff4499',"#3700ff"]  

n = int(input())
coins = np.random.randint(0,2,n)
# print('正面出现次数 =',len(coins[coins==1]))

dice = np.random.randint(1,7,n)
A = []
for i in range(1,7):
    A.append(len(dice[dice==i]))
B = ['1','2','3','4','5','6']
f1 = plt.subplot(1,2,1)
f1.bar(B,A,
        width = 0.4
        )
f1.set_title('骰子1-6次数',fontsize = 20)
f1.set_xlabel('骰子点数',fontsize = 10)
f1.set_ylabel('次数',fontsize = 10)
f1.grid(axis='y',alpha=0.5,linestyle='--')
for x,y in zip(B,A):
    f1.text(x,y,str(y),ha='center',va='bottom',fontsize=10)
f2 = plt.subplot(1,2,2)
f2.pie(A,
       labels = B,
       colors = colors,
       autopct = '%1.1f%%'
       )
f2.set_title('各点数占比',fontsize=20)
plt.tight_layout()
plt.show()
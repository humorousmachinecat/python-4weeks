import matplotlib.pyplot as plt
from matplotlib import rcParams     
rcParams['font.family'] = 'SimHei'

#创造图表，设置大小
plt.figure(figsize=(10,5))

#设置数据
country = ['US','CN','JP','GM','ID','UK']
gdp = [100,90,77,56,50,43]

#绘制条形图
plt.barh(country,gdp,                            
         color = 'blue'
         )

#添加标题
plt.title('各国gdp',color = 'red',fontsize = 20)

#添加坐标轴标签
plt.xlabel('gdp',fontsize=10)
plt.ylabel('country',fontsize=10)

#添加网格线
plt.grid(axis='x',alpha=0.5,color = 'black',linestyle = '--') 

#自动优化排版
plt.tight_layout()

#显示图表 
plt.show()
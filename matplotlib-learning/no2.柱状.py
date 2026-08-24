import matplotlib.pyplot as plt
from matplotlib import rcParams     
rcParams['font.family'] = 'SimHei'

#创造图表，设置大小
plt.figure(figsize=(10,5))

#设置数据
month = ['1月','2月','3月','4月']
sales = [100,50,77,56]

#绘制柱状图
plt.bar(month,sales,label = '产品A',           
         color = 'orange',
         width = 0.4
         )

#添加标题
plt.title('2025销售趋势',color = 'red',fontsize = 20)

#添加坐标轴标签
plt.xlabel('月份',fontsize=10)
plt.ylabel('销售额',fontsize=10)

#添加图例
plt.legend(loc='upper left')

#添加网格线
plt.grid(axis='y',alpha=0.5,color = 'blue',linestyle = '--') 
        #grid(Ture)表示x轴y轴表格都生成。axis = 'y'表示生成垂直于y轴直线。alpha表示透明度。color表示颜色，linestyle表示不同的线

#设置刻度字体大小
plt.xticks(rotation=0,fontsize=12)  #rotation为旋转角度，fontsize为字体大小
plt.yticks(rotation=0,fontsize=12)

#设置y轴范围
plt.ylim(0,160)                     #plt.ylim(start,end)

#在每个数据点上显示数值
for x,y in zip(month,sales):
    plt.text(x,y+1,str(y),ha='center',va='bottom',fontsize=10)

#自动优化排版
plt.tight_layout()

#显示图表 
plt.show()
import matplotlib.pyplot as plt
from matplotlib import rcParams     
rcParams['font.family'] = 'SimHei'

#创造图表，设置大小
plt.figure(figsize=(10,5))

#数据
things = ['其他','睡觉','运动','娱乐','学习']
times = [6,9,2,3,4]
colors = ['#66b3ff','#99ff99','#ffcc99','#ff9999','#ff4499']    
#调整配色
explode = [0.1,0,0,0,0]                 #设置突出块的位置

#创造饼状图
plt.pie(times,labels = things,
        autopct = '%1.1f%%',
        startangle = 90,                #调整初始角度
        colors = colors,
        # wedgeprops = {'width':0.5},   #变成圆环图
        pctdistance = 0.6,              #设置百分比的位置
        explode = explode,              #设置突出块
        shadow = True                   #添加阴影
        ) 

#添加标题
plt.title('一天的时间',color = 'red',fontsize = 20)

#添加文字
# plt.text(0,0,'总计:100%',ha = 'center')
#ha = 'center'表示水平居中  va = 'bottom'表示垂直方向在底部

#自动优化排版
plt.tight_layout()

#显示图表 
plt.show()
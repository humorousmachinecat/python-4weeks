import numpy as np
import matplotlib.pyplot as plt

T = 1
N = 500 
dt = T/N                    #每一步步长

np.random.seed(0)
x = np.random.randn(N)
dW = np.zeros(N)        #预处理，防止循环添加。
#dw = np.zeros(N)生成了1条Brownian路径，dw = np.zeros((M,N))生成了M条Brownian路径
W = np.zeros(N)

dW = np.array(np.sqrt(dt)*x)    
# 从0变到1一共500步，一行存了500个值,一共1000行，对应1000条路径
# 增量 dW 服从均值为 0、方差为 dt 的正态分布
# x ~ N(0,1)  dw = sqrt(dt)*x --> dw ~ N(0,sqrt(dt))

W = np.cumsum(dW)
#累加得到路径

t = np.linspace(0,T,N+1)        
# t = [0,dt,2dt,3dt,...,T] 共有501个元素,此时W中每行只有500个元素

W = np.concatenate(([0],W))
# 满足W[0] = 0,也满足了shape(t)=shape(W)
# print(np.shape(t),np.shape(W))

# 画布朗运动路径
plt.figure(figsize=(12,8))
plt.plot(t, W, 
         'r-',
         label = 'brownian path')

plt.legend(loc='upper left')
plt.xlabel('t', fontsize=10)
plt.ylabel('W(t)', fontsize=10, rotation=0)
plt.show()


# 将Brownian封装进函数
# def brownian(T,N):
#     dt = T/N                
#     np.random.seed(0)
#     x = np.random.randn(N)
#     dW = np.zeros(N)        
#     W = np.zeros(N)
#     dW = np.array(np.sqrt(dt)*x)    
#     W = np.cumsum(dW)
#     t = np.linspace(0,T,N+1)        
#     W = np.concatenate(([0],W))
#     plt.figure(figsize=(12,8))
#     return(W,t)
import numpy as np
import matplotlib.pyplot as plt

T = 1
N = 500
dt = T/N                
np.random.seed(0)
x = np.random.randn(N)
dW = np.zeros(N)        
W = np.zeros(N)

dW = np.array(np.sqrt(dt)*x)    
W = np.cumsum(dW)
t = np.linspace(0,T,N+1)        
W = np.concatenate(([0],W))

ito = np.sum(W[0:N]*dW)
strat = np.sum(((0.5*(W[0:N]+W[1:N+1]))+0.5*np.sqrt(dt)*np.random.randn(N))*dW)

print(ito,strat)

itoerr = np.abs(ito - 0.5*(W[N]**2-T))
straterr = np.abs(strat - 0.5*(W[N]**2))

print(itoerr,straterr)
# plt.plot(t, W, 
#         'r-',
#         label = 'brownian path')

# plt.legend(loc='upper left')
# plt.xlabel('t', fontsize=10)
# plt.ylabel('W(t)', fontsize=10, rotation=0)
# plt.show()
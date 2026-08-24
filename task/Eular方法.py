import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return(-x/y)

def Eular(x0,y0,end,alpha):
    N = int((end-x0)/alpha)
    x = np.linspace(x0,end,N)
    y = np.array([y0])
    for i in range(N-1):
        y = np.append(y,y[i]+alpha*f(x[i],y[i]))
    return x,y

x0 = 0
y0 = -1
end = 1
alpha = 1e-5
x,y = Eular(x0,y0,end,alpha)
plt.plot(x,y)
plt.show()


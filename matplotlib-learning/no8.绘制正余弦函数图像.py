import matplotlib.pyplot as plt
import numpy as np

#定义x范围，0到4Π范围内取100个点
x = np.linspace(-2*np.pi,2*np.pi,100)
# y1 = np.sin(x)
# plt.plot(x,y1)

y2 = np.cos(x)
plt.plot(x,y2)
plt.show()
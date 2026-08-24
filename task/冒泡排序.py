import numpy as np

def bubble(x):
    n = len(x)
    a = 0
    while a < n:
        b = a + 1
        while b < n:
            if x[a] > x[b]:
                x[a] = x[a] + x[b]
                x[b] = x[a] - x[b]
                x[a] = x[a] - x[b]
                b = b + 1
                continue
            b = b + 1
        a = a + 1
    return x



x = [2,3,4,1,6,55,77,88,2323]
n = len(x)
bubble(x)
for y in range(0,n):
    print(x[y])
print('\n')   
arr = np.random.randint(1,30,15)
bubble(arr)
for y in range(0,10):
    print(arr[y])
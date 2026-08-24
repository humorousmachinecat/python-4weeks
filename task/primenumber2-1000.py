for x in range(2,1001):
    sum = 0
    for y in range(2,x):
        if x%y == 0:
            sum = sum+1
    if sum==0:
        print(x)
        
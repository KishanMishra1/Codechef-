import numpy as np

n=np.array([1,2,3,4,5])
m=np.array([10,9,8,7,6])

k=int(input())
for i in range(k//2):
    print(*n)
    print(*m)
    m+=10
    n+=10

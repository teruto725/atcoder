import numpy as np
H,N = map(int,input().split())
m = list()
dp = np.zeros(H+1)
for i in range(N):
    m.append(list(map(int,input().split())))
for i in range(N):
    Hi = H-i 
    dpi = int()
    zeroflg = 0
    for j in range(len(m)):
        if (Hi + m[j][0]) >=H:
            zeroflg +=1
        else:
            


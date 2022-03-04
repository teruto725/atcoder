import numpy as np
N,M = map(int,input().split())
li = np.zeros((N,N),dtype="int8").tolist()

for i in range(M):
    Ai, Bi =map(int,input().split())	
    li[Ai-1][Bi-1] = 1
    li[Bi-1][Ai-1] = 1

que = list()
idx = list(range(0,N)) #index list for second loop

maxC = 0

while True:
    if len(idx) == 0:
        break
    startfriend = idx.pop(0)
    que.append(startfriend)
    count = 0# firends num
    while True:
        print(idx)
        if len(que) == 0:
            break
        num =  que.pop(0)
        print(str(num)+"の友達探す")
        for j in reversed( range(len(idx))):
            if li[num][idx[j]] == 1 :
                #print("友達"+str(idx[j]))
                que.append(idx[j])
                idx.pop(j)
                count += 1 
    
    print("count:"+str(count))
    if maxC < count:
        maxC = count
     
print(maxC+1)
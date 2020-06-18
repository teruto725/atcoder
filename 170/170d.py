n=int(input())
a = list(map(int,input().split()))
que = []
flg = []
p3flg = True
for ai in a:
    #print("------"+str(ai))
    if len(que) == 0:
        que.append(ai)
        flg.append(0)
    else:
        j = 0
        p3flg = True
        while True:
            if len(que) == j:
                if p3flg:
                    que.append(ai)
                    flg.append(0)
                break
            if ai == que[j]:
                flg[j] = 1
                break
            if ai % que[j] == 0:
                break
            if que[j] % ai == 0:
                if p3flg:
                    que[j] = ai
                    flg[j] = 0
                else:
                    que.pop(j) 
                    j -= 1
                p3flg = False

            j+= 1
            
print(len(que)-sum(flg))
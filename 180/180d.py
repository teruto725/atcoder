X,Y,A,B = map(int,input().split())
nowx = X
nowexp = 0
while True:
    #print(nowx)
    if nowx >= Y:
        print(nowexp-1)
        break
    if nowx < B:
        nowx = nowx *A
        nowexp += 1
    else:
        nowexp += (Y - nowx -1) //B
        print(nowexp)
        break
N,Y = map(int,input().split())
flag = False
for i in range(N+1):
    for j in range(N+1):
        if Y<(10000*i+5000*j):
            break
        elif (Y-(10000*i+5000*j))/1000==N-i-j:

            print(str(i)+" "+str(j)+" "+str(N-i-j))
            flag = True
            break
    if flag == True:
        break
else:
    print("-1 -1 -1")

N,X,Y = map(int,input().split())
li = [0]*(N-1)
for i in range(0,N-1):
    for j in range(i+1,N):
        dis = min(j-i,abs(j-(X-1))+1+abs(i-(Y-1)),abs(i-(X-1))+1+abs(j-(Y-1)))
        li[dis-1] += 1
for ans in li:
    print(ans)
N,M = map(int,input().split())
li = list(map(int,input().split()))
if N>=sum(li):
    print(N-sum(li))
else:
    print(-1)
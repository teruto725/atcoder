N,M = map(int,input().split())
li = list(map(int,input().split()))
li.sort(reverse=True)
if li[M-1] >= sum(li)/(4*M):
    print("Yes")
else:
    print("No")

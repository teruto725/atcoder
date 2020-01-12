N,K,M = map(int,input().split())
li = list(map(int,input().split()))
want = M*N

s = sum(li)
sub = want - s
if sub > K:
    print("-1")
elif sub >= 0:
    print(sub)
else:
    print(0)


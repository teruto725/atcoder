#n段の上り方のバリエーションはフィボナッチ数列になっている

N, M = map(int,input().split())
alist = list()
for _ in range(M):
    alist.append(int(input()))


li = {}
li[0] = 1

for i in range(1,N+1):
    if len(alist)>=1 and i ==  alist[0]:
        li[i] = 0
        alist.pop(0)
    else:
        if i == 1:
            li[i] = 1
        else:
            li[i] = ((li[i-1] + li[i-2])%(10**9+7))
print(li[N]%(10**9+7))
N=int(input())
A = list(map(int,input().split()))
m = 0
ans = 0
for i in range(2,1001):
    c=0
    for ai in A:
        if ai%i == 0:
            c+= 1
    if c >= m:
        m = c
        ans = i
print(ans)

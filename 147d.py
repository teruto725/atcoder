N = int(input())
li = list(map(int,input().split()))
ans = 0

for i in range(N-1):
    for j in range(i+1,N):
        ans += (li[i]^li[j])
print(ans%(1000000007))

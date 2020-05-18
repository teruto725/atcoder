N,M = map(int,input().split())
H = list(map(int,input().split()))
ans = [1]*N
for i in range(M):
    Ai,Bi = map(int,input().split())  
    Ai -=1
    Bi -=1
    if H[Ai] == H[Bi]:
        ans[Ai]=0
        ans[Bi]=0
    elif H[Ai] > H[Bi]:
        ans[Bi]=0
    elif H[Bi] > H[Ai]:
        ans[Ai]=0
print(sum(ans))

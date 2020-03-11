N,M = map(int,input().split())
ans = ["a"]*N
flg = False
for i in range(N):
    s,c = map(int,input().split())
    if ans[s] == "a":
        ans[s] == str(c)
    elif ans[s] != "a":
        flg = True
if flg:
    print("-1")
else:
    for num in ans:
        if num =
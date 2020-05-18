n,k = map(int,input().split())
ans = {}
for i in range(k):
    di=int(input())	
    li = list(map(int,input().split()))
    for l in li:
        ans[str(l)] = "0"
count = 0
for i in range(1,n+1):
    if str(i) not in ans.keys():
        count += 1
print(count)
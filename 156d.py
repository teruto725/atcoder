
n,a,b = map(int,input().split())
m = 10**9+7
li =  [1]

for i in range(2,n+1):
    p = li[i-2]*i
    if p >= m:
        li.append(p-((p//m)*m))
    else:
        li.append(p)
print(li[n]*)


K,N = map(int,input().split())


a = list(map(int,input().split()))	
maxdis = a[0]+K-a[-1]
alldis = a[0]+K-a[-1]
a.sort()
for i in range(1,N):
    alldis += a[i] - a[i-1]
    maxdis = max(maxdis,a[i]-a[i-1])
print(alldis-maxdis)
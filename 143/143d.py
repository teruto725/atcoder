
import bisect
N = int(input())
L = list(map(int,input().split()))
count = 0
L.sort()
for i in range(N-2):
    for j in range(i+1,N-1):
        count += bisect.bisect(L,L[i]+L[j]-1)-j-1
print(count)

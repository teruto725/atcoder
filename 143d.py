import copy
import bisect
N = int(input())
L = list(map(int,input().split()))
count = 0
L.sort()
for i in range(N-1):
    for j in range(i+1,N):
        print(L[i])
        print(L[j])
        maxi = L[i] + L[j] -1
        mini = abs(L[i] - L[j]) +1
        cL = copy.copy(L)
        if j < i: 
            cL.pop(i)
            cL.pop(j)
        else:
            cL.pop(j)
            cL.pop(i)
        mi = bisect.bisect_left(cL,mini)
        ma = bisect.bisect_left(cL, maxi)
        ma = N - ma -1
        print("mi"+str(mi)+"ma"+str(ma))
        if ma >= mi:
            count += ma-mi

                 
            
print(count)

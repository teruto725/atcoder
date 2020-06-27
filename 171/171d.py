import collections

N = int(input())
A = list(map(int,input().split()))
Q = int(input())
counter = collections.Counter(A)
Asum = sum(A)
ans = list()
for i in range(Q):
    B,C = map(int,input().split())
    if B in counter:
        num = counter.pop(B)
        Asum = Asum + (C-B)*num
        counter[C] = counter[C]+num
    ans.append(Asum)
for a in ans:
    print(a)
    	

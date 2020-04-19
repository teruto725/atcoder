import collections
N=int(input())
li = input().split()
c = collections.Counter(li)
for i in range(1,N+1):
    if str(i) in c.keys():
        print(c[str(i)])
    else:
        print(0)
    
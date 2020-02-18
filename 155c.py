import collections
import itertools
N=int(input())
di = dict()
l = list()
for i in range(N):
    l.append( input())

c = collections.Counter(l)
ct = c.most_common()
m = ct[0][1]
li = list()
for t in ct:
    if m == t[1]:
        li.append(t[0]) 
    else:
        break
lis = sorted(li)
for s in lis:
    print(s)

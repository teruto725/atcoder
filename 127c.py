n,m = map(int,input().split())

lmax = 0
rmin = 100000
for i in range(m):
    l,r = map(int,input().split())
    if l > lmax:
        lmax = l
    if r < rmin:
        rmin = r
if rmin >= lmax:
    print(rmin+1-lmax)
else:
    print(0)

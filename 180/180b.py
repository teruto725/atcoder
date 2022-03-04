N=int(input())
xli = list(map(int,input().split()))
m = 0
s = 0
s2 = 0
for x in xli:
    s += abs(x)
    m = max(m,abs(x))
    s2 += abs(x)**2
print(s)
print(s2**(1/2))
print(m)
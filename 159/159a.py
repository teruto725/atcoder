import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
n,m = map(int,input().split())
ans = 0
if n >= 2:
    ans += combinations_count(n, 2)
if m >= 2:
    ans += combinations_count(m, 2)
print(str( ans ))

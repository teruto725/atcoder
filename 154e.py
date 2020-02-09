
import math

def c(n, r):
    return math.factorial(n) // math.factorial(n - r)

def Knum(k):
    Knum = 1
    for i in range(k):
        Knum = Knum * (9-i)
    return Knum

N=int(input())
K=int(input())
l=len(str(N))


ans = 0
ans += c(l-1,K)*Knum(K)
if K >1:
    ans += c(l-1,K-1)*Knum(K-1)*int(str(N)[0]-1)
else:
    ans += int(str(N)[0])
if K > 2:
    ans += c(l-2,K-2)*Knum(K-2)*int(str(N)[0]-2)
else:
    ans += int(str(N)[1])
notzero=str(N).index("0")


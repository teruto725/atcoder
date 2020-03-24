from math import factorial
N,A,B = map(int,input().split())
m = 10**9+7
li =  [1]

def calc(n):
    ret = 1
    for i in range(n):
        ret = ret * (N - i) % MOD
    return ret * pow(factorial(n), MOD - 2, MOD) % MOD

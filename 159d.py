import collections
import math

def combinations_count2(n, memo):
    if n <= 1:
        return 0
    if n in memo.keys():
        return memo[n]
    else:
        memo[n]= math.factorial(n) // (math.factorial(n - 2) * math.factorial(2))
        return memo[n]


n = input()
li = input().split()
c = collections.Counter(li)
memo = dict()
Sum = 0
for cv in c.values():
    Sum += combinations_count2(cv,memo)
for l in li:
    print(Sum - c[l] +1)

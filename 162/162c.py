import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

N = int(input())
count = 0
for i in range(1,N+1):
    for j in range(i,N+1):
        for k in range(j,N+1):
            if i == j == k:
                count += gcd(i,j,k)
            elif i != j != k:
                count += gcd(i,j,k)*6
            else:
                count += gcd(i,j,k)*3

print(count)
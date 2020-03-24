import math
import itertools


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


n=int(input())
d = make_divisors(n)
len = len(d)
if len % 2 == 0:
    print((d[int(len/2)]-1)+(d[int(len/2-1)]-1))
else:
    print((d[int((len-1)/2)]-1)+(d[int((len-1)/2)]-1))

def gcd(a,b):
    x = max(a,b)
    y = min(a,b)
    if x%y == 0:
        return y
    else:
        while x%y != 0:
            z = x%y
            x = y
            y = z
        else:
            return z

def lcm(m,n):
    return int(m * n/gcd(m,n))

a,b = map(int,input().split())
print(lcm(a,b))

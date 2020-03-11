n,a,b = map(int,input().split())
mod = n % (a+b)
d = n//(a+b)
if mod >= a:
    mod = a
print( d*a + mod)
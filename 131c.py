
def gcd(a,b):
  if b>a:
    a,b=b,a
  while a%b:
    a,b=b,a%b
  return b


A,B,C,D = map(int,input().split())
mul = C*D//gcd(C,D)
mi = (A-1) // mul
ma = B // mul
mv = ma-mi
#print(mv)
ci = (A-1) // C
ca = B // C
cv = ca-ci
#print(cv)
di = (A-1) // D
da = B // D
dv = da-di
#print(dv)
print(B-A-cv-dv+mv+1)
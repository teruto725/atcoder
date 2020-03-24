def ans(a,b,n):
    return((a*n)+(b*len(str(n))))

a,b,x = map(int,input().split())
premaxn = (x+x%a)/a
an = 0
for pren in reversed(range(int(premaxn)+1)):
    #print(ans(a,b,pren))
    if ans(a,b,pren) < x:
        an = pren
        break
if an > 1000000000:
    print(1000000000)
else:
    print(an)

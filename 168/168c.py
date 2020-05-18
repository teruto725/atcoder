import math
A,B,H,M = map(int,input().split())	
hun = H*60 + M
doji = (hun / 720)*360
#print(doji)
dohun = (M/60)*360
#print(dohun)
if abs(doji - dohun) <= 180 :
    ans = A**2+B**2-2*A*B*math.cos(math.radians(abs(doji-dohun)))
elif doji - dohun >=0:
    ans = A**2+B**2-2*A*B*math.cos(math.radians(360-doji+dohun))
else:
    ans = A**2+B**2-2*A*B*math.cos(math.radians(360-dohun+doji))

print(math.sqrt(ans))
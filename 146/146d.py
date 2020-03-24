import math
a,b,x = map(float,input().split())
bottom = (x/(a*a))/b * a * 2.0
if bottom <= a:
    print(math.degrees(math.atan2(b,bottom)))
else :
    high = (b - (x/(a*a)))*2
    print(math.degrees(math.atan2(high,a)))

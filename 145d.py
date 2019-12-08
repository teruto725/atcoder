import math
def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)
def comb(x,y):
    return (math.factorial(permutations_count(x, y))/math.factorial(y))



x,y = map(int,input().split())
if x<y:
    temp = x
    x = y
    y = x
count = 0

if x == y and x % 3 ==0 and y % 3 == 0:
    print(int(comb((x/3)*2,x/3)%1000000007))
else:
    while True:
        print(count)
        if x == y*2:
            print(int(comb(y+(count*2), count)%1000000007))
            break
        elif x > y*2:
            print(0)
            break
        else:
            x =x - 3
            y =y - 3
            count +=1

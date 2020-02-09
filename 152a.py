x,y = map(int,input().split())	
if y > x:
    for i in range(y):
        print(x, end="")
else:
    for i in range(x):
        print(y, end="")
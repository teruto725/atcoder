x,y,z = map(int,input().split())	
if (x == y and x != z) or (x == z and x != y) or (y == z and x != y):
    print("Yes")
else:
    print("No") 
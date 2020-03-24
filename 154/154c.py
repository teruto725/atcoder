N=int(input())
li = list(map(int,input().split()))	
num = {}
for l in li:
    if str(l) not in num :
        num[str(l)] = 1
    elif num[str(l)]==1:
        print("NO")
        break
else:
    print("YES")





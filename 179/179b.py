N = int(input())
count = 0
flg = False
for i in range(N):
    
    d1,d2 = map(int,input().split())
    if d1 == d2:
        count += 1
        if count ==3:
            flg = True
    else:
        count = 0
if flg:
    print("Yes")
else:
    print("No")
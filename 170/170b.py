x,y = map(int,input().split())
flg = True
for i in range(0,x+1):
    if 2*i+4*(x-i) == y:
        print("Yes")
        flg = False
        break
if flg:
    print("No")

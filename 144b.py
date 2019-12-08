a=int(input())
f = True
for i in range(1,10):
    for j in range(1,10):
        if i * j == a:
            print("Yes")
            f = False
            break
    if f == False:
        break
if f == True:
    print("No")

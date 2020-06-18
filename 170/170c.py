li = input().split()
x = int(li[0])
n = int(li[1])
if n == 0:
    print(x)
else:
    li = list(map(int,input().split()))
    count = 0
    while True:
        if  x - count not in li:
            print(x-count)
            break
        elif x+count not in li:
            print(x+count)
            break 

        count+= 1
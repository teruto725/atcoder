x=int(input())
items = [100,101,102,103,104,105]
list = [1]
if x == 100 or x == 101 or x == 102 or x == 103 or x == 104 or x == 105:
    print(1)
elif x <100:
    print(0)
else:
    for i in range(99):
        list.append(0)
    for i in range(6):
        list.append(1)
    for i in range(94):
        list.append(0)
    for i in range(200,x+1):
        for item in items:
            if list[i-item] == 1:
                list.append(1)
                break
        else:
            list.append(0)

    print(list[x])

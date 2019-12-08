N = int(input())
li = list()
for i in range(N):
    Ai = int(input())
    Alist = list()
    for j in range(Ai):
        x,y = map(int,input().split())
        Alist.append([x-1,y])
    li.append(Alist)
num =(2**(N))
while True:
    ok = True
    num -=1
    numlist = format(num, 'b')
    #print(list(numlist))
    zero = str()
    if N != len(numlist):
        for i in range(N-len(numlist)):
            zero += "0"

        numlist = zero + numlist
    #print(numlist)
    for i in range(len(numlist)):
        if numlist[i] == "1":
            for j in range(len(li[i])):
                if int(numlist[li[i][j][0]]) != li[i][j][1]:
                    ok = False
                    break
        if ok == False:
            break
    if ok == True:
        print(numlist.count("1"))
        break
    if num == 0:
        print(0)
        break

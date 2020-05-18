N,M = map(int,input().split())

li = []
for i in range(M):
    li.append(list(map(int,input().split())))
ans = [0] * (N+1)
#print(ans)
que = [1]
#print(li)
def saiki ():
    global que
    global li
    global ans
    #print(que)
    q = que.pop(0)
    count = 0
    while True:
        
        if count == len(li):
            break
        #print(li)
        #print(count)
        if li[count][0] == q and ans[li[count][1]] == 0:
            que.append(li[count][1])
            ans[li[count][1]] = q
            li.pop(count)
        elif li[count][1] == q and ans[li[count][0]] == 0:
            que.append(li[count][0])
            ans[li[count][0]] = q
            li.pop(count)
        else:
            count += 1
    if len(que) == 0:
        print("Yes")
        for ai in ans:
            if ai != 0:
                print(ai)
    else:
        saiki()

saiki()

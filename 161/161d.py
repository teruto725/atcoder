def pat(K,count,keta,num):
    #print(str(num)+":"+str(count)+":"+str(keta))
    if count == -1:
        return -1
    elif keta == 1:
        if count == K-1:
            print(num)
            return -1
        else:
            return (count+1)
    else:
        if (int(num[-1])) -1 >= 0:
            count = pat(K,count,keta-1,num+str(int(num[-1])-1))
        count = pat(K,count,keta-1,num+num[-1])
        if (int(num[-1])+1) <= 9:
            count = pat(K,count,keta-1,num+str(int(num[-1])+1))
            
    return count


K = int(input())
count = 0
ans = list()
keta = 0

while True:
    keta += 1
    for i in range(1,10):
        count = pat(K,count,keta,str(i))
        #print(count)
        if count  == -1:
            break
    if count == -1:
        break
        


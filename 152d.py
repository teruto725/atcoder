def map_all(es):
    return all([e == es[0] for e in es[1:]]) if es else False

def calc(num):
    ans = 1
    for i in range(num):
        ans += 10**(i+1)
    return ans

def check(num,N):
    s =str(num)[-1]
    for _ in range(len(str(N))-2):
        s += "0"
    s += str(num)[0]
    if int(s) < N:
        return True
    else:
        return False

    
N = int(input())
strN = str(N)
lengN = len(strN)
count = 0
for num in range(1,N+1):
    snum = str(num)
    if int(snum[-1]) != 0:
        if len(snum) == 1:
            count += 1#一桁なら確定で＋１
            while True:
                snum += snum[0]
                if int(snum) <= N:
                    count +=2
                else:
                    break
        elif N < 99:
            if int(snum[1]+snum[0]) <= N:
                count += 1
        else:
            first = snum[-1]
            last = snum[0]
            leng = len(snum)
            if int(first) < int(strN[0]):
                count += calc(lengN-2)
            else:                
                if int(first) == int(strN[0]) and check(num,N) :
                    count += (N-num//10)  #1の位を0にした値
                count += calc(lengN-3)
    print(snum +" "+ str(count))
print(count) 



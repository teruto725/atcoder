import collections
n=int(input())
dlist = list(map(int,input().split()))
c = collections.Counter(dlist)#{0:1,1:3,2:4}
keys = sorted(c.keys())#[0,1,2,4]
max = keys[len(keys)-1]#2
ok = True#check
if c[0] != 1:#1
    ok = False
    print(0)
count = 0
if ok:
    for k in keys:#数字が並んでるか
        #print(str(k)+str(count))
        if count != k:
            print(0)
            ok = False
            break
        count += 1

ans = 1
if ok:
    for i in range(1,max):
        ans = ans*(pow(c[i],c[i+1])%998244353)
        ans = ans % 998244353
    print(ans)

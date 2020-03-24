N = int(input())
li = list(map(int,input().split()))	
mi = 10000000000
for i in range(1,100):
    hp = 0
    for j in range(0,len(li)):
        hp += (i-li[j])**2
    if mi >= hp:
        mi = hp
print(mi)
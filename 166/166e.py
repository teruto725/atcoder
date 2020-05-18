N = int(input())
li = list(map(int,input().split()))	
di = {}
count = 0
for i in range(N):
    if str((i+1)-li[i]) in di.keys(): 
        count += di[str((i+1)-li[i])]
    if str(i+1+li[i]) in di.keys(): 
        di[str(i+1+li[i])] += 1
    else:
        di[str(i+1+li[i])] = 1
print(count)
N=int(input())
li = list(map(int,input().split()))	
mini = li[0]
count = 0
for num in li:
    if mini >= num:
        count += 1
        mini = num
print(count)
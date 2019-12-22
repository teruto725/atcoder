N = int(input())
li = list(map(int,input().split()))
count = 1
flag = False
for i in range(N):
    if li[i] == count:
        count += 1
        flag = True
if flag:
    print(N-count)
else:
    print("-1")

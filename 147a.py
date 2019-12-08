li = list(map(int,input().split()))
ans = 0
for i in li:
    ans += i
if ans >= 22:
    print("bust")
else:
    print("win")

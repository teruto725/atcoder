
n=int(input())
s = list(map(int,input().split()))
ans = 0
for i in range(9):
    for j in range(9):
        for k in range(9):
            for l in range(len(s)):
                if i == s[l]:
                    for m in range(l,len(s)):

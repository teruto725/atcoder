import collections
N = int(input())
stock = dict()
ans = 0
for i in range(N):
    c="".join(sorted(input()))
    if c in stock:
        ans += stock[c]
        stock[c] += 1
    else:
        stock[c] = 1
print(ans)
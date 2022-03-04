m = 998244353

N,K = map(int,input().split())
s=set()
for i in range(K):
    i1,i2 = map(int,input().split())
    s.update(set(range(i1,i2+1)))
memo = [-1]*(N+1)
def saiki(n):
    if n == 1:
        return 1
    elif n <=0:
        return 0
    elif memo[n] != -1:#use memo
        return memo[n]

    count = 0
    for i in s:
        count += saiki(n-i)
        count = count % m
    memo[n] = count
    
    return count
print(saiki(N))


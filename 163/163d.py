def touSum(a,l):
    return int(((l-a+1)*(a+l))/2)
N,K = map(int,input().split())
con = 0
for i in range(K,N+1+1):
    con += touSum((1+N)-i,N) -touSum(1,i-1)+1
print(con%(10**9+7))
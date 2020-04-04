N,K = map(int,input().split())
m1 = N % K
m2 = K- N% K 
print(min(m1,m2))
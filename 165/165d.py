A,B,N = map(int,input().split())
if B-1 >=N:
    print(int(A*N/B)-A*int(N/B))
else:
    print(int(A*(B-1)/B)-A*int((B-1)/B))

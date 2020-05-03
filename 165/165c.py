m = 0
N,M,Q = map(int,input().split())

li = []
for _ in range(Q):
    li.append( list(map(int,input().split())))

def check(A):
    global m
    n = 0
    for s in li:
        print(A)
        if A[s[1]-1]-A[s[0]-1] == A[s[2]-1]:
            n += A[s[3]]
    m = max(n,m)   

def saiki(A,knum):
    if knum == N:
        return
    for i in range(A[knum-1],M+1):
        A[knum] = i
        check(A)
        saiki(A,knum+1)


A = [1 for _ in range(N)]

for i in range(1,M+1):
    A[0] = i 
    saiki(A,1)
    

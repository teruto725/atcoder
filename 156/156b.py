N,K = map(int,input().split())
val = 1
if N == 1:
    print(1)
else:
    for i in range(1,N):
        val = val * K
        if val > N:
            print(i)
            break
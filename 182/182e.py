H,W,N,M = map(int,input().split())
field = [[0]*W]*H
for i in range(N):
    x,y = map(int,input().split())
    field[x,y] = 1
for i in range(M):
    field[x,y] = 2
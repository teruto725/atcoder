R,C = map(int,input().split())
r1 = abs(R-8)
c1 = abs(C-8)
if max(r1 , c1) % 2 == 0:
    print("white")
else:
    print("black")
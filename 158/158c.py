A,B = map(int,input().split())
ran = B*10
for i in range(ran,ran+10):
    if int(i * 0.08) == A:
        print(i)
        break
else:
    print(-1)
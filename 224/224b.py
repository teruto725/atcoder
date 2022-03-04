H,W = map(int,input().split())
A = list()
for i in range(H):
  li = list(map(int,input().split()))
  A.append(li)
def func():
  for i1 in range(0,H-1):
    for i2 in range(i1+1,H):
      for j1 in range(0,W-1):
        for j2 in range(j1+1,W):
          if A[i1][j1] + A[i2][j2] > A[i2][j1]+A[i1][j2]:
            return "No"
  else:
    return "Yes"

print(func())

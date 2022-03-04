N = int(input())
XY = list()
for i in range(N):
  XY.append(list(map(float, input().split())))

count = 0
for i in range(N-2):
  for j in range(i+1,N-1):
    for k in range(j+1,N):

      if (XY[i][1]-XY[j][1]) * (XY[i][0]-XY[k][0]) == (XY[i][0]-XY[j][0]) * (XY[i][1]-XY[k][1]):
        continue
      elif (XY[i][1]-XY[j][1]) * (XY[i][0]-XY[k][0]) == -1 *  (XY[i][0]-XY[j][0]) * (XY[i][1]-XY[k][1]):
        continue
      count += 1
        
print(count)
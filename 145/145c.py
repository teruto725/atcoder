import math


class point():
    def __init__(self, x,y):
        self.x = x
        self.y = y



n=int(input())
points = list()
for i in range(n):
    x,y = map(int,input().split())
    points.append(point(x,y))


sum = 0
for i in range(n-1):
    for j in range(i+1,n):
        sum += math.sqrt((points[i].x-points[j].x)**2+(points[i].y-points[j].y)**2)
print(sum*2/n)

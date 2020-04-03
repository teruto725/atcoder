import copy
import sys
from collections import deque
import numpy

input = sys.stdin.readline
H,W= map(int,input().split())
input_maze = [list(input()) for _ in range(H)]
ans = 0
for i in range(H):
    for j in range(W):
        if input_maze[i][j] ==".":
            queue = deque()
            queue.append([i,j,0])#最初の△
            maze = copy.deepcopy(input_maze)
            while True:
                if len(queue) ==0:
                    tem_ans = point[2]
                    break
                point=queue.popleft()#queueの先頭座標+何回移動したかの取得
                maze[point[0]][point[1]] = point[2] 
                
                #print(numpy.array(maze))    
                if point[0] > 0 and maze[point[0]-1][point[1]]==".":#上
                    queue.append([point[0]-1,point[1],point[2]+1])
                if point[0] < len(maze)-1 and maze[point[0]+1][point[1]]==".":#下
                    queue.append([point[0]+1,point[1],point[2]+1])
                if point[1] > 0 and maze[point[0]][point[1]-1]==".":#左
                    queue.append([point[0],point[1]-1,point[2]+1])
                if point[1] < len(maze[point[0]])-1 and maze[point[0]][point[1]+1]=="." :#右
                    queue.append([point[0],point[1]+1,point[2]+1])
            ans = max(ans,tem_ans)
print(ans)
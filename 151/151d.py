import copy
import sys
input = sys.stdin.readline
H,W= map(int,input().split())
maze = [list(input()) for _ in range(H)]
maze = [l[:len(maze[0])-1] for l in maze]
ans = 0
for i in range(H):
    for j in range(W):
        if maze[i][j] !="#":
            queue = [[i,j,0]]#最初の△
            tem_ans = 0
            while True:
                if len(queue) ==0:
                    tem_ans = point[2]
                    break
                point=queue.pop(0)#queueの先頭座標+何回移動したかの取得
                maze[point[0]][point[1]] = str(point[2]) 
                #print(np.array(maze))
                if point[0] > 0 and maze[point[0]-1][point[1]]!="#" and maze[point[0]-1][point[1]]!=str(point[2]-1):#上
                    queue.append([point[0]-1,point[1],point[2]+1])
                if point[0] < len(maze)-1 and maze[point[0]+1][point[1]]!="#" and maze[point[0]+1][point[1]]!=str(point[2]-1):#下
                    queue.append([point[0]+1,point[1],point[2]+1])
                if point[1] > 0 and maze[point[0]][point[1]-1]!="#" and maze[point[0]][point[1]-1]!=str(point[2]-1):#左
                    queue.append([point[0],point[1]-1,point[2]+1])
                if point[1] < len(maze[point[0]])-1 and maze[point[0]][point[1]+1]!="#" and maze[point[0]][point[1]+1]!=str(point[2]-1):#右
                    queue.append([point[0],point[1]+1,point[2]+1])
                
            ans = max(ans,tem_ans)
print(ans)
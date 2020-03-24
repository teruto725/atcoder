import copy
import numpy
def move(maze):
    is_move = False
    cp_maze = copy.deepcopy(maze)
    for i in range(H):
        for j in range(W):
            if cp_maze[i][j]=="X":
                if i > 0 and cp_maze[i-1][j]==".":#上
                    maze[i-1][j] = "X"
                    is_move = True
                    #print("上")
                if i < len(cp_maze)-1 and cp_maze[i+1][j]==".":#下
                    maze[i+1][j] = "X"
                    is_move = True
                    #print("下")
                if j > 0 and cp_maze[i][j-1]==".":#左
                    maze[i][j-1] = "X"
                    is_move = True
                   # print("左")
                if j < len(cp_maze)-1 and cp_maze[i][j+1]=="." :#右
                    maze[i][j+1] = "X"
                    is_move = True
                    #print("右")
    return is_move


H,W= map(int,input().split())
input_maze = [list(input()) for _ in range(H)]
ans = 0
for i in range(H):
    for j in range(W):
        if input_maze[i][j] ==".":
            dis = 0
            maze = copy.deepcopy(input_maze)
            maze[i][j]="X"
            while True:
                is_move = move(maze)
                if is_move:
                    dis += 1
                else:
                    ans = max(dis,ans)
                    break
print(ans)
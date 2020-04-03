data = [list(map(int,input().split())) for _ in range(3)]

N = int(input())
for _ in range(N):
    bn = int(input())
    for i in range(3):
        for j in range(3):
            if bn == data[i][j]:
                data[i][j] = 0
ans = "No"
for i in range(3):
    if data[i][0] == data[i][1] == data[i][2] == 0:ans = "Yes"
    if data[0][i] == data[1][i] == data[2][i] == 0:ans = "Yes"
if data[0][0] == data[1][1] == data[2][2]==0:ans ="Yes"
if data[0][2] == data[1][1] == data[2][0] == 0 :ans="Yes"
print(ans)
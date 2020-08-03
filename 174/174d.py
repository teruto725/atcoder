N= int(input())
C = input()
red = 0
white = 0
for i in range(N):
    if C[i] == "W":
        white +=1
    else:
        red += 1
c = 0
for i in range(red):
    if C[i] == "W":
        c +=1
print(c)
X=int(input())
m = 100
count =1
while True:
    m = int(m*1.01)
    if m >= X:
        print(count)
        break
    count += 1

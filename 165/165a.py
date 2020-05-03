k=int(input())
a,b = map(int,input().split())
ans = 0
while True:
    ans += k
    if a<=ans<=b:
        print("OK")
        break
    if b <ans:
        print("NG")
        break
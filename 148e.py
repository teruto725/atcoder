N = int(input())
d = 2
count = 0
if N % 2 == 1:
    print(0)
else:
    for i in range(N+1):
        d *= 5
        if d > N:
            break
        count += N // d
    print(count)

N,M = map(int,input().split())
a = list(map(int,input().split()))
ansli = list()
count = 1

a = list(set(a))[::-1]
a0 = a.pop(0)
while True:
    num = int(a0*(count+0.5))
    if num >M:
        break
    else:
        ansli.append(num)
    count += 1

for ai in a:
    stack = list()
    for ansj in ansli:
        if (ansj/ai) % 0.5 == 0.0:
            stack.append(ansj)
    ansli = stack
print(len(ansli))
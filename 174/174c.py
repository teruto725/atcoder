K = int(input())


if (K%10) % 2 == 0:
    print(-1)
elif (K%10) % 5 == 0:
    print(-1)
"""
else:
    num = 7
    for i in range(K):
        if num % K == 0:
            print(str(i+1))
            break
        num = (num *10 + 7) % K
    else:
        print(-1)
"""
li = list(range(10))
for i in range(10): 
    li[(K*i)%10] = i    



num = K
for i in range(K):
    if num == 0:
        print(i)
        break
    num += li[(7-num%10)%7]*K
    num = int(num/10)
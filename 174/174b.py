#K = int(input())
for K in range(100):
    #print(K)
    if (K%10) % 2 == 0:
        pass
        #print(-1)

    elif (K%10) % 5 == 0:
        pass
        #print(-1)
    else:
        num = 7
        for i in range(100000):
            if num % K == 0:
                print(str(i+1)+)
                break
            num = num *10 + 7
        else:
            print(-1)


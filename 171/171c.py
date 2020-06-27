char = 'abcdefghijklmnopqrstuvwxyz'


N=int(input())
stack = 26
bstack = 0
length = 1
while True:
    if stack >=N:
        order = N-bstack-1#何番目de
        #print(order)
        counter = 0
        ans = ""
        for i in reversed(range(length)):
            if i == 0:
                ans = ans + char[order]
            elif order > 26**(i):
                div = int(order/26**(i))#3
                ans = ans + char[div]
                order = order - div*26**(i)
            else:
                ans = ans+ "a"
        print(ans)
        break    


    bstack = stack
    length += 1
    stack = stack+26**length#702
import math
def siki(Xs,n):
    ans = 0
    for i in range(len(Xs)):
        ans += int(Xs[i]) * n**(len(Xs)-1-i)
    return ans

Xs= input()
X =int(Xs)
M = int(input())
d = int(max( list(str(Xs))))
l = len(Xs)
if l == 1:
    if l > M:
        print(0)
    else:
        print(1)
else:
    #print(pow(M,1/(l-1)))
    n_max = M+1#nの最大値
    #print(n_max)
    left_n = d
    right_n =n_max
    while True:
        #print("====")
        #print(right_n)
        #print(left_n)
        middle_n = (left_n+right_n) //2
        middle_value = siki(Xs,middle_n)
        if middle_value > M:
            right_n = middle_n
        else:
            left_n = middle_n
        if right_n == left_n+1:
            print(left_n-d)
            break

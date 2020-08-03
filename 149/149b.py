a,b,k = map(int,input().split())
ansa = 0
if a + b <k:
    print("0 0")
elif a < k:
    ansa =0
    ansb = b-(k-a)
    print(str(ansa)+" "+str(ansb))
else:
    ansa = a-k
    ansb = b
    print(str(ansa)+" "+str(ansb))
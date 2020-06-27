N,M,K = map(int,input().split())
a = list(map(int,input().split()))	
b = list(map(int,input().split()))

A = [0]
B = [0]
A.extend(a)
B.extend(b)
time = sum(A)
ai = len(A)-1
bi = 0
con = 0
flg = None
count = 0
while True:
    #print("---------")
    #print(str(ai)+":"+str(bi))
    if time > K:
        if flg is not None:
            con = max(con,flg-1)
            flg = None
        
        if ai == 0:
            break
        time -=A[ai]
        ai -= 1
    else:
        #print("b")
        flg = ai+bi
        time +=B[bi]
        bi += 1
        if bi == len(B):
            if time > K:
                if flg is not None:
                    con = max(con, flg-1)
                pass
            else:
                con = max(con,ai+bi-1)
            break
    #print(flg)
print(con)
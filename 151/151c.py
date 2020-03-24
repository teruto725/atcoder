N,M = map(int,input().split())
di = {}
pe = 0
ac = 0
for i in range(M):
    inp = input().split(" ")
    if inp[1] == "WA":
        if inp[0] in di:#登場してる
            if di[inp[0]] >= 1:#間違えてる
                di[inp[0]] += 1
            #else ACsareteru
        else:#初めて出た
            di[inp[0]] = 1#辞書に登録される　1
            
            
    else:
        if inp[0] in di:#登場してる
            pe += di[inp[0]]#間違い回数をたす
        di[inp[0]] = 0#3:0
        
for v in di.values():#{: ~~~~~~  } [3,0,1,0] di.value() di.key()
    if v == 0:
        ac += 1
print(str(ac)+" "+str(pe))
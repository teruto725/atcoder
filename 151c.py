N,M = map(int,input().split())
di = {}
pe = 0
ac = 0
for i in range(M):
    inp = input().split(" ")
    if inp[1] == "WA":
        if inp[0] in di:
            if di[inp[0]] >= 1:
                di[inp[0]] += 1
        else:
            di[inp[0]] = 1
            
            
    else:
        if inp[0] in di:
            pe += di[inp[0]]
            di[inp[0]] = 0
        di[inp[0]] = 0
        
for v in di.values():
    if v == 0:
        ac += 1
print(str(ac)+" "+str(pe))
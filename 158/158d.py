s=input()
q = int(input())
toggle = "ok"
top = ""
last = ""

for i in range(q):
    si = input().split()
    if si[0] == "1":
        if toggle == "ok":
            toggle = "re"
        else:
            toggle = "ok"
    else:
        if si[1] == "1" and toggle == "ok":
            top += si[2] 
        elif si[1] == "2" and toggle == "re":
            top += si[2] 
        elif si[1] == "1" and toggle == "re":
            last += si[2]
        elif si[1] == "2" and toggle == "ok":
            last += si[2]
if toggle == "ok":
    retop = ''.join(list(reversed(top)))
    print(retop, end="")
    print(s,end="")
    print(last,end="")
else:
    relast = ''.join(list(reversed(last)))
    print(relast,end="")
    res = ''.join(list(reversed(s)))
    print(res,end="")
    print(top,end="")    

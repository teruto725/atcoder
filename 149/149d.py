def calcPoint(me,opp,R,S,P):
    if me == "r":
        if opp == "s":
            return R
        else:
            return 0
    elif me == "s":
        if opp == "p":
            return S
        else:
            return 0
    else:
        if opp == "r":
            return P
        else:
            return 0

def saiki(K,R,S,P,Tlist,copypat): 
    #print(copypat)
    plist =[]

    if len(Tlist) == len(copypat):#底まで行っちゃってる場合
        #print(calcPoint(Tlist[-1],copypat[-1],R,S,P))
        return calcPoint(copypat[-1],Tlist[-1],R,S,P)

    if len(copypat) <K:#Kよりもcopypatが小さかったら
        plist.append(saiki(K,R,S,P,Tlist,copypat+"r"))
        plist.append(saiki(K,R,S,P,Tlist,copypat+"s"))
        plist.append(saiki(K,R,S,P,Tlist,copypat+"p"))
    else:
        if copypat[-K] != "r":
            plist.append(saiki(K,R,S,P,Tlist,copypat+"r"))
        if copypat[-K] != "s":
            plist.append(saiki(K,R,S,P,Tlist,copypat+"s"))
        if copypat[-K] != "p":
            plist.append(saiki(K,R,S,P,Tlist,copypat+"p"))

    if copypat == "":
        return max(plist)
    else:
        nowpoint = calcPoint(copypat[-1],Tlist[len(copypat)-1],R,S,P)
        #print(max(plist)+nowpoint)
        return max(plist)+nowpoint

N,K = map(int,input().split())
R,S,P = map(int,input().split())
Tlist = input()
print(saiki(K,R,S,P,Tlist,""))


count = 0
def saiki(imin,haba,s):
    global count
    if haba <=4:
        return
    print(s[imin:imin+haba])
    if int(s[imin:imin+haba])%2019==0:
        print("yes")
        count += 1
        if haba %2 == 0:
            saiki(imin,int(haba/2),s)
            saiki(imin+int(haba/2),int(haba/2),s)
        else:
            saiki(imin,int((haba+1)/2),s)
            saiki(imin+int((haba+1)/2),int((haba+1)/2),s)
    else:
        saiki(imin,haba-1,s)

    if int(s[imin+1:imin+1+haba])%2019 == 0:
        print("yes")
        count += 1
        if haba %2 == 0:
            saiki(imin+1,int(haba/2),s)
            saiki(imin+1+int(haba/2),int(haba/2),s)
        else:
            saiki(imin+1,int((haba+1)/2),s)
            saiki(imin+1+int((haba+1)/2),int((haba+1)/2),s)
    else:
        saiki(imin+1,haba-1,s)
        


s = input()
saiki(0,len(s),s)
print(count)
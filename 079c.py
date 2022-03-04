

def tansaku(abcd,ans,num,formula):
    if num == 4:
        if ans == 7:
            print(formula)
            return 0
    #+のとき
    ans +=  abcd[num]
    formula += "+"+str(abcd[num])
    ansaku(abcd,ans,formula,num+1)
    # - のとき
    ans -= abcd[num]
    formula += "-"+str(abcd[num])
    ansaku(abcd,ans,formula,num+1)
abcd = list(map(int,list(input())))
print(li)
stack  = 0
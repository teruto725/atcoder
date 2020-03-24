def kaibun(s):
    flg = False
    if len(s) % 2 == 0:
        if s[0:int((len(s)/2))] == s[int(len(s)/2):len(s)][::-1]:
            flg =True
    else:
        
        if s[0:int((len(s)-1)/2)] == s[int((len(s)+1)/2):len(s)][::-1]:
            flg =  True
    return flg
s = input()
ans = "No"

if kaibun(s):
    if kaibun(s[0:int((len(s)-1)/2)]) and kaibun(s[int((len(s)+1)/2):len(s)]):
        ans = "Yes"
print(ans)
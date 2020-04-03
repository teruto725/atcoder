N,M = map(int,input().split())
ans = ["a"]*N
flg = False
for i in range(M):
    s,c = map(int,input().split())
    if ans[s-1] == "a":
        ans[s-1] = str(c)
    elif ans[s-1] != "a" and ans[s-1] != str(c):
        flg = True
if flg:
    print("-1")
else: 
    one_flg = True 
    a = ""  
    if len(ans) == 1:
        print(ans[0])
    else:
        for num in ans:
            if num == "a":
                if one_flg:
                    a+="1"
                else:
                    a += "0"
            elif num == "0":
                if one_flg:
                    print("-1")
                    break
            else:
                a += num
            one_flg = False   
        else:
            print(a)



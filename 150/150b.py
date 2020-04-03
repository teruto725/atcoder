N = int(input())
S = input()
count =0
flg = 0
for s in S:
    if s == "A":
        flg = 1
    elif s == "B" and flg == 1:
        flg =2
    elif s =="C" and flg ==2 :
        count +=1
        flg =0
    else:
        flg = 0
print(count)
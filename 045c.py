S = input()#入力
ans = 0 #答え
bin_len = len(S)-1#間の数2進数の大きさ

if bin_len == 0:#一文字のときは直接出力
    print(S)
else:
    for i in range(2**bin_len):
        bin_str = format(i, 'b')#2進変換
        temp_l = len(bin_str)#長さ
        for j in range(0,bin_len-temp_l):
            bin_str = "0"+bin_str
        
        print("bin_str"+bin_str)# 00 01 10 11 str型 s[0]

        stack = S[0] #文字列 
        for j in range(len(bin_str)):
            if bin_str[j] == "0":
                stack = stack + S[j+1]#12
            else:
                ans += int(stack) 
                stack = S[j+1]
        ans += int(stack)
        #print("stack"+str(ans))
    print(ans)
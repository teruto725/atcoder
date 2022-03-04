# bit全探索
s = input()

# 全ての数式の合計
ans = 0

# bit全探索
for i in range(2 ** (len(s)-1)):
    tmp = 0
    for j in range(len(s)):
        if (i >> j) & 1:  # bitが1なら+をいれる
            print(i)
            print(i >> j)
            ans += tmp*10 + int(s[j]) 
            tmp = 0
        else:
            tmp = tmp*10 + int(s[j])
    ans += tmp

print(ans)
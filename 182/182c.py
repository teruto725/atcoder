N = input()
ans = 100
for i in range(1,2**len(N)):
    bin_str = format(i, 'b')
    bin_str = "0"*(len(N)-len(bin_str))+bin_str
    summ = 0
    c = 0
    #print(bin_str)
    for i in range(len(bin_str)):
        if bin_str[i] == "1":
            summ += int(N[i])
        else:
            c += 1
    if summ % 3 == 0 and ans > c:
        ans = c
if ans == 100:
    print(-1)
else:
    print (ans)
        
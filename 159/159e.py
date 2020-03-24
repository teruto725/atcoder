H,W,K = map(int,input().split())
choco = [input() for l in range(H)]
num =(2**(H-1))

white_count = list()
min_div_count =10**6
for i in range(num):
    bin_str = format(i, 'b')
    zero = str()
    if H != len(bin_str):
        for i in range(H-len(bin_str)):
            zero += "0"
        bin_str = zero + bin_str
    white_count = [0 for s in bin_str if s == "1"]
    white_count.append(0)
    div_count=len(white_count)-1
    j = 0
    while j < W:
        block_count = 0
        for k in range(len(bin_str)):
            if bin_str[k] == "1":
                block_count += 1
            white_count[block_count] += int(choco[k][j])
            if white_count[block_count] > K:
                div_count +=1
                white_count = [0 for s in bin_str if s == "1"]
                white_count.append(0)
                break
        else:
            j+=1
    if min_div_count > div_count:
        min_div_count = div_count
print(min_div_count)
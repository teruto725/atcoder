H,W,K = map(int,input().split())
choco = [input().split() for l in range(H)]
num =(2**(H))
for i in range(num):
    numlist = format(num, 'b')
    li = 
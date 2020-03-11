def re(H):
    if H == 1:
        return 1
    else:
        return re(H//2)*2+1

H = int(input())
print(re(H))

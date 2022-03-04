S = input()
ms = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(S)):
    if i % 2 == 0 and S[i] not in ms:
        print("No")
        break
    elif i % 2 == 1 and S[i] in ms:
        print("No")
        break
else:
    print("Yes")
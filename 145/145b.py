n=input()
s=input()
if len(s) % 2 == 0 and s[:int(len(s)/2)] == s[int(len(s)/2):]:
    print("Yes")
else:
    print("No")

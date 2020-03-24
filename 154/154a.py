s=input().split()
li = list(map(int,input().split()))
s1=input()
if s1 == s[0]:
    print(str(li[0]-1) + " "+str(li[1]))
else:
    print(str(li[0])+" "+str(li[1]-1))
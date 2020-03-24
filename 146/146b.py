a=int(input())
s=input()
list= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
slist = [c  for c in s]
ans = str()
for si in slist:
    i = list.find(si)
    ans += list[(i+a)%26]
print(ans)

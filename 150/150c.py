N= int(input())
p = input().replace(" ","")
q = input().replace(" ","")
kai = [1]
for i in range(2,N):
    kai.append(kai[-1]*i)
def calc(s,N):
    count =0
    nlist = [str(i) for i in range(1,N+1)]
    for i in range(N-1):
        
        idx = nlist.index(s[i])
        nlist.remove(s[i])
        count += (idx)*(kai[len(nlist)-1])
        
    return count+1

print(abs(calc(p,N)-abs(calc(q,N))))

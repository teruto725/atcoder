n,k = map(int,input().split())
li = list(map(int,input().split()))
mux = 0
s = 0

def div(n):
    return (n + 1)/2

for i in range(k):
    s += div(li[i])
mux = s 	

for i in range(k,len(li)):
    s -= div(li[i-k])
    s += div(li[i])
    if s > mux:
        mux = s
print(mux)
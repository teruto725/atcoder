N,K = map(int,input().split())

def f(a):
    li = [x for x in list(str(a))]
    g2_s = sorted(li)
    g1_s = list(reversed(g2_s))#大きい順
    return  int("".join(g1_s)) - int("".join(g2_s))

ai = N
for _ in range(K):
    ai = f(ai)
print(ai)
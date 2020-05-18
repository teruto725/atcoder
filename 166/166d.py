X = int(input())
Acount = 0
Bcount = 0
di= {}
def func(i):
    return i**5
for i in range(5000):
    di[str(func(i))] = str(i)
preA = int(X **(1/5))-1000
while True:
    funcA = preA**5
    if funcA-X>=0 and str(funcA-X) in di.keys():
        print(str(preA)+" "+di[str(funcA-X)])
        break
    elif X-funcA>= 0 and str(X-funcA) in di.keys():
        print(str(preA)+" -"+di[str(X-funcA)])
        break
    preA += 1
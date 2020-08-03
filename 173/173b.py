di ={"AC":0,"WA":0,"TLE":0,"RE":0}
N = int(input())
for i in range(N):
    s = input()
    di[s] += 1
for key in di:
    print(key+" x "+str(di[key]))

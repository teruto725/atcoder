N=int(input())
S =input()
count =0

Bcount = S.count("B")
for i in range(0,N-1):
    for j in range(i+1,N):
        if (S[i] == "R" and S[j] == "G") or (S[i] == "G" and S[j] == "R") :
            count += Bcount
            if j+(j-i) <N  and S[j+(j-i)] == "B":
                count  -=1
            if i-(j-i) >=0 and S[i-(j-i)] =="B":
                count -=1
            if (i+j)%2 ==0 and S[int((i+j)/2)] == "B":
                count -=1
print(count)
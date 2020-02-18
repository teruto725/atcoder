n=int(input())
li = list(map(int,input().split()))	
for num in li:
    if num % 2 == 0:
        if num % 3 != 0 and num % 5 != 0:
            print("DENIED")
            break
else:
    print("APPROVED")
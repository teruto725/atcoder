li = input()
count = 0
if len(li) % 2 == 0:
    for i in range(int(len(li)/2)):
        if li[i] != li[len(li)-i-1]:
            count += 1
else:
    for i in range(int((len(li)-1)/2)):
        if li[i] != li[len(li)-i-1]:
            count += 1
print(count)

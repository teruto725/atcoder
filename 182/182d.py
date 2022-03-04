N=int(input())
A = list(map(int,input().split()))
ans = 0 #最大の座標
max_sum = None 
sum_stack = 0 #これまでの配列合計
last_num = 0#前回エポックの最後の座標
for i in range(N):
    #print(last_num)

    #last_numの更新
    last_num_back = sum_stack + last_num + A[i]
    #sum_stackの更新
    sum_stack += A[i]
    #max_sumの更新
    if max_sum is None:
        max_sum = sum_stack
    elif sum_stack > max_sum:
        max_sum = sum_stack #値の合計の最大値これを前回のlastnumに足したのがこのエポックの最大値
    #ansの更新
    best_num = max_sum + last_num 

    last_num = last_num_back
    if ans is None:
        ans = best_num
    elif ans < best_num:
        ans = best_num

print(ans)
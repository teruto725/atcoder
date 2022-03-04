N = int(input())
A = list(map(int,input().split()))
MOD = 998244353
stack = [0]*10
for i,a in enumerate(A):
  if i == 0:
    stack[a] = 1
    continue
  next_stack = [0]*10
  for j,s in enumerate(stack):
    next_stack[(j * a)%10] += (stack[j]% MOD)
    next_stack[(j + a)%10] += (stack[j]% MOD)
  stack = next_stack
for s in stack:
  print(s % MOD)




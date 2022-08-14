# 2次元配列Aから行、列を任意の回数削除したときに2次元配列Bと一致するか判定する

H1,W1 = map(int,input().split())
A = []
for i in range(H1):
  A.append(list(map(int,input().split())))
  
H2,W2 = map(int,input().split())
B = []
for i in range(H2):
  B.append(list(map(int,input().split())))

def find_index(arr):
  index = []
  for i in range(len(arr)):
    if arr[i] == 1:
      index.append(i)
  return index
  
def get_patterns():
  patters = []
  for num in (2**W1):
    bit_str = bin(num)[2:]
    if bit_str.count("1") == W2:
      patters.append(find_index(bit_str))
      
patterns = get_patterns()

def check(lineA,pattern,lineB):
  for i in range(len(pattern)):
    if lineA[pattern[i]] != lineB[i]:
      return False
  else:
    return True

stack = []

for j in range(H2):
  lineB = B[j]
  if j == 0:
    for i in range(H1):
      lineA = A[i]
      temp = []
      for pattern in patterns:
        if check(lineA,patterns[j],lineB):
          temp.append(patterns[j])
        stack.append(temp)
  else:
    new_stack = []
    for pattern in stack:
      for i in range(H1):
        lineA = A[i]
        if check(lineA,pattern,lineB):
          new_stack.append(pattern)
    stack = new_stack
    
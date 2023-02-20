def f_1(x):
  c=0
  f=[2,1]
  while f[-1]<=x:
    f.append(f[-1]+f[-2])
    c+=1
  return f

f=f_1(1E9)
n=int(input())
for i in range(n):
  v=int(input())
  if v in f:
    print(f)
  else:
    print("0")
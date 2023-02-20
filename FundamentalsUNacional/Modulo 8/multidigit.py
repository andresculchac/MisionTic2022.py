l=[]
def f_1(x):
  Lista=["1","2","3","4","5"]
  inicio=str(x)
  for j in Lista:
      if j  not in inicio:
       return False
  
  return True

while True:
  e=int(input())
  if e==0:
    break
  else:
    l.append(e)
for i in l:
  if f_1(i):
    print("Multidigito")
  else:
    print("No es multidigito")
#preguntar multidigito
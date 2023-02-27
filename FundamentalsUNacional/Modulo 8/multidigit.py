init_input=[]
def multi_ulti(x):
  desarrollo=["1","2","3","4","5"]
  kilom=str(x)
  for k in desarrollo:
      if k  not in kilom:
       return False
  return True
#retorno importante
while True:
  xy=int(input())
  if xy==0:
    break
  else:
    init_input.append(xy)
for bv in init_input:
  if multi_ulti(bv):
    print("Multidigito")
  else:
    print("No es multidigito")

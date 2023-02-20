def panVolicas(ingreso):
  red_u=["a","e","i","o","u"]

  for xy in red_u:
    if xy not in ingreso:
      return False
  return True

#esta si 

nana=int(input())
for _ in range(nana):
  simp = input()
  nana-=1


  #entrada 11 
  if panVolicas(simp):
    print("Panvolica")
  else:
    print("No es panvolica")

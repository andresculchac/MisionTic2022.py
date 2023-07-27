def sourcepanvolica(ingreso):
  red_u=["a","e","i","o","u"]

  for xy in red_u:
    if xy not in ingreso:
      return False
  return True

#esta si 

panvolica11=int(input())
for _ in range(panvolica11):
  simp = input()
  panvolica11-=1


  #entrada 11 
  if sourcepanvolica(simp):
    print("Panvolica")
  else:
    print("No es panvolica")

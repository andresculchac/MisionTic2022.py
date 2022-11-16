'''
table = [[3,2,8],[5,1,4],[6,9,0]]
numero = int(input("ingrese el numero que desea buscar en la tabla"))
encontrado = False

for filas in table:
  for columnas in filas:
    if columnas == numero:
      encontrado = True
      break
    if encontrado == True:
      encontrado == True
      break
  
if encontrado == True:
  print("el numero fue encontrado")
if encontrado == False:
  print("el numero no fue encontrado :(")


    #imprimir solo las primeras filas osea solo los nombres
personas = [["juancho cadavid",28,1.75],["pachito suarez",32,1,68],["juanita lopez",19,1,70]]
tamaño = len(personas)

for i in range(0,tamaño):
  print(personas[i][0])
'''   

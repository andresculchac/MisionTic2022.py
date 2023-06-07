pedirEntrada = int(input())
listaReal = [] #En lista real tiene que agregarse los inputs que deseemos
realListaDivisores = []
definitivo = []


for i in range(1,pedirEntrada+1):
    requestInput = int(input()) #The types of variable  can change
    addList = listaReal.append(requestInput)

def realDivisores(num1)->list:
  for j in range(len(listaReal)):
    for i in range(1,listaReal[j]):
      if listaReal[j] % i == 0:
        realListaDivisores.append(i)
    if sum(realListaDivisores) == listaReal[j]:
      definitivo.append(True)
      realListaDivisores.clear()
    else:
      definitivo.append(False)
      realListaDivisores.clear()
  return definitivo
(realDivisores(listaReal)) #Ejecutando la funcion
#Ciclo para la impresion bonita.
for i in range(len(definitivo)):
    if definitivo[i] == True:
        print(listaReal[i],"es perfecto")
    else:
       print(listaReal[i],"no es perfecto")

    


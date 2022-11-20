

def inputs(): #hacer una funcion que si pongo un numero input pues se ejecute tres veces #tipos de inputs
    request = int(input())
    while request>0:
      j = input() #Se evalua el tipo de entrada que se le va a poner ej: int, float, str
      listaX.append(j)
      request -= 1
    print(listaX)

listaX = ['obelix'] #sufijo 'ix' significa origen "galo"   



# for i in range(len(listaX)): #Ciclo que analiza en una lista letra por letra.
#     for i in listaX[i]:
#         if i == listaX[0]
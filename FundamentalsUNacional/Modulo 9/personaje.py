
#Todos se tienen que convertir con la primera en mayuscula.

def inputs(): #hacer una funcion que si pongo un n inputs pues se ejecute n veces #tipos de inputs
    request = int(input())
    while request>0:
      j = input().capitalize() #Se evalua el tipo de entrada que se le va a poner ej: int, float, str ademas se pone el manejo de strings
      listaX.append(j)
      request -= 1
    print(listaX)

listaX = [] #sufijo 'ix' significa origen "galo"   
inputs()



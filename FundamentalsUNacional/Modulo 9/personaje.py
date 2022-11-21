
#Todos se tienen que convertir con la primera en mayuscula.

def inputs(): #hacer una funcion que si pongo un n inputs pues se ejecute n veces #tipos de inputs
    request = int(input())
    while request>0:
      j = input().capitalize() #Se evalua el tipo de entrada que se le va a poner ej: int, float, str ademas se pone el manejo de strings
      a.append(j)
      request -= 1
    #print(a) #Guia para ver como van las salidas

a = []  
inputs()
almacen = []

for i in range(len(a)):
    if a[i][-1:] == "a": #algoritmo para identificar a los indios
        amabilidad = a[i][-1:]
        almacen.append(amabilidad)
        if amabilidad == "a":
            print("Indio")
            continue
    
    robar =a[i][-2:]
    almacen.append(robar)
    if robar == "ix":
        print("Galo")
    elif robar == "us":
        print("Romano")
    elif robar == "ic":
        print("Godo")
    elif robar == "as":
        print("Griego")
    elif robar == "af":
        print("Normando")    
    elif robar == "is" or robar == "ax":
        print("Breton")
    elif robar == "ez":
        print("Hispano")
    else:
      print("Desconocido")
    
            
            
            

#print(almacen)


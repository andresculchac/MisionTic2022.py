def inputs(): #hacer una funcion que si pongo un n inputs pues se ejecute n veces #tipos de inputs
    request = int(input())
    while request>0:
      j = input().upper() #Se evalua el tipo de entrada que se le va a poner ej: int, float, str ademas se pone el manejo de strings
      a.append(j)
      request -= 1
    print(a) #Guia para ver como van las salidas

a = []  
inputs()
    


#Modificacion para la formula 
#lo siguiente que tengo que hacer es pasar el codigo a una funcion donde reciba
#la lista de la funcion Listend()


def listend(): #Esta funcion recibe inputs y termina cuando le pones un -1
    variableX = True
    while variableX:
        variableJ = input()
        if variableJ == '-1':
            variableX = False
        listaX.append(variableJ)
    listaX.pop(-1) #Sirve para eliminar el 0 que a veces puede causar interferencias
    #print(listaX) # este print es de referencia para ver como se esta llendo la lista :3



'''
Encontre a la solucion hypepares pasandolos a strings de modo que toca ver como los adaptamos
De este punto aprendi bastante acerca de ciclos y su funcionamiento mas de cerca y como utilizar for in range
entendiendo un poco mas de for in
#aprendi acerca de no cometer errores en las comparaciones porque no es lo mismo == que = y es algo que me confundi y estaba comparando
y por eso no me cambiana la variable de booleanos(gracias a dios me ayudo la tutora muy observadora 👀)
'''
listaX = [] #Es raro porque si esta variable no exixte antes de la funcion dice que no esta declarada XD
listend()
indice = 0

encontrador = True
for i in range(len(listaX)):
    for i in listaX[i]:
        if int(i) % 2 == 0:
            encontrador = True
        elif int(i)%2 != 0:
            encontrador = False
            break
            
    if encontrador == False:
        print("No es hyperpar")
        encontrador = True
    elif encontrador == True:
        print("Hyperpar")
    indice += 1
    
    

    
      


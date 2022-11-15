#Modificacion para la formula 
listaX = []
def listend(): #Esta funcion recibe inputs y termina cuando le pones un -1
    variableX = True
    while variableX:
        variableJ = int(input())
        if variableJ == -1:
            variableX = False
        listaX.append(variableJ)
    listaX.pop(-1) #Sirve para eliminar el 0 que a veces puede causar interferencias
    print(listaX) # este print es de referencia para ver como se esta llendo la lista :3



x = [2080]


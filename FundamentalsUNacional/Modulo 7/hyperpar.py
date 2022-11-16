#Modificacion para la formula 
listaX = []

def listend(): #Esta funcion recibe inputs y termina cuando le pones un -1
    variableX = True
    while variableX:
        variableJ = input()
        if variableJ == '-1':
            variableX = False
        listaX.append(variableJ)
    listaX.pop(-1) #Sirve para eliminar el 0 que a veces puede causar interferencias
    print(listaX) # este print es de referencia para ver como se esta llendo la lista :3

#listend()

'''
Encontre a la solucion hypepares pasandolos a strings de modo que toca ver como los adaptamos
'''
x = ['2080','256','88888']
j = [2080 , 256,88888]
indice = 0


for j in range(len(j)):
    #print(x[indice])
    for i in x[indice]:
        print(i)
    indice += 1
    #print(type(i))
    

    
      

# print(caracter)
#     if int(caracter)%2 == 0:
#       print("Hyperpar")  
#     else:
#       print("no es par")
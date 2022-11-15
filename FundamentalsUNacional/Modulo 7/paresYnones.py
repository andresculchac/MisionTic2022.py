import math 
listaX = []
def listend(): #Esta funcion recibe inputs y termina cuando le pones un 0
    variableX = True
    while variableX:
        variableJ = int(input())
        if variableJ == 0:
            variableX = False
        listaX.append(variableJ)
    listaX.pop(-1) #Sirve para eliminar el 0 que a veces puede causar interferencias
    #print(listaX) # este print es de referencia para ver como se esta llendo la lista :3

listend()

#uso de formulas
def fdex (X):
    return math.sqrt(2+(5*X))
def gdex(Y):
    return (4+Y)**3

def complete():
    for i in listaX:
        if i % 2 == 0:
            print(fdex(gdex(i)))
        else:
            print(gdex(fdex(i)))
complete()   

'''
De este ejercicio aprendi que hay que organizar bien el uso de las funciones por ejemplo si no ponemos en orden las funciones no va a dar
ningun resultado por eso recordar que el codigo tiene un orden de lectura.
Tambien aprendi un poco mas el uso de return y los usos generales
y porque es diferente el return a solo ejecutar la funcion 
en general me parecio mas util el return porque podemos usarlos en mas cosas y es un poco mas sencillo retornar y creo que tiene un mejor uso
de lectura 
'''       

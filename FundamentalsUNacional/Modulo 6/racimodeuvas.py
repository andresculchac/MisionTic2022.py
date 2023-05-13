#2023-1
#Este parece muy facil
#Primero inputs con 0
import math
variableX = True
lista = []

while variableX:
    variableJ = int(input())
    if variableJ == 0:
        variableX = False
    lista.append(variableJ)
lista.pop(-1)

# #Falta agregar la formula triangular 
a = 1
b = 1



for i in lista:
    c = -(i*2) #De acuerdo a la formula protagonista
    n = (1)-(4*a*c)
    minRaiz = (-b-math.sqrt(n))/2*a #discriminate negativo
    plusRaiz = (-b+math.sqrt(n))/2*a
    if plusRaiz > 0 and plusRaiz.is_integer():
        print("Puede ser un racimo ideal")
    else:
        print("No puede ser un racimo ideal")






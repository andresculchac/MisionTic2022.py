"""
Puedo encontrar los detalles de la lista en el
inicio
Debe haber un patron y lo puedo encontrar con
mas ejemplos de listas
"""

#Desarrollo

lista = list()
solicitar = int(input())
for i in range(solicitar):
    num = float(input())
    lista.append(num)

N = len(lista)
contador = 0
if N>2:
    for i in range(1,N-1):
        if sum(lista[:i]) == sum(lista[i:]):
            contador += 1
else:
    for i in range(1,N):
        if sum(lista[:i]) == sum(lista[i:]):
            contador += 1

print(contador)

        

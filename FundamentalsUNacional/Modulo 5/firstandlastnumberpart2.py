#Pedir el primero y el ultimo numero de una serie de numeros que me pidan

numeros = input()
lectura = len(numeros)
contador = 0
#hacer un ciclo que me entre uno por uno cada numero
#
lista = []
for numero in numeros:
    contador += 1
    if contador == 1:
        agregar = lista.append(numero)
    if contador == lectura:
        agregar = lista.append(numero)

print(int(lista[0]+lista[1]))


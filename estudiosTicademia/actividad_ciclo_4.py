'''
En este codigo vamos a trabajar con diccionarios 
Date : 6/8/2022
Code of test
output        = {"t":66,"u":72,"d":90,"r":84,"j":36,"g":50,"s":94,"q":62,"f":35}
output_letter = d p h u i e t q

'''

import json

entrada      = json.loads(input())
lista = input() #Lista de entrada
lista_orden = []
contador = 0

for i in lista: 
    if i in entrada.keys():
        lista_orden.append(i)   #aqui sacamos el orden de la lista pero en el orden que es de la lista y no del for 


for llave, valor in entrada.items():
    if llave in lista:
        contador= contador + valor  #y con este sacamos los valores que realmente no importan el orden porque las claves son unicas 
 
print(contador)
lista_to_string = " ".join(lista_orden)
print(lista_to_string)
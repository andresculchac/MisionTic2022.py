'''
En este codigo vamos a trabajar con diccionarios 
Date : 6/8/2022

'''
# importar esta libreria nos permite convertir un string con
# forma de diccionario a un diccionario de verdad 
import json

entrada      = json.loads(input())
#print(type(entrada)) 
lista = input() #Lista de entrada

contador = 0
lista2 = []

for llave,valor in entrada.items():
    if llave in lista:
        contador = contador + valor
        lista2.append(llave)

print(contador)
print(lista2)

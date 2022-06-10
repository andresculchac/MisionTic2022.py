'''
En este codigo vamos a trabajar con diccionarios 
Date : 6/8/2022

Code of test
output        = {"t":66,"u":72,"d":90,"r":84,"j":36,"g":50,"s":94,"q":62,"f":35}
output_letter = d p h u i e t q

'''
# importar esta libreria nos permite convertir un string con
# forma de diccionario a un diccionario de verdad 


entrada = {"t":66,"u":72,"d":90,"r":84,"j":36,"g":50,"s":94,"q":62,"f":35}
#print(type(entrada)) 
lista = "d p h u i e t q" #Lista de entrada
lista_en_list = ["d", "p", "h", "u", "i", "e", "t", "q"]
lista_orden = []
contador = 0

'''
# The items() method will return each item in a dictionary, as tuples in a list.
# i think that i must think in the challenge three as through comparation
# Tengo que solucionar el orden de comparacion
# idear un plan para que se pongan en orden como la salida de output_letter
# en debuggin podemos ver como entra el valor con t 66 puesto que es la que comienza 
# entonces hay radica nuestro problema 
# ya lo tenemos casi hecho el paso siguente es que lista tenga prioridad y eso como lo hacemos 
# pienso que primero debemos hacer un for para reconocer las letras que estan en la lista, luego mandarles hacer el for 
# siguiente para que hagan la impresion 

'''
# hacer un programa que saque las letras conforme la lista que tenemos de entrada y sacarlas por orden de lista //COMPLETE
# hacer un programa que sume las entradas de arriba 
# pregunta del dia porque lista no esta en llave 🤨 xq pues llave solo toma un solo valor cuando esta en for 😔
# for llave, valor in entrada.items():
#     if llave in lista:
#         print(llave)
   
# pues tenemos la primera parte ahora solo falta la suma de los numeros 

for i in lista: 
    if i in entrada.keys():
        lista_orden.append(i)


          

for llave, valor in entrada.items():
    if llave in lista:
        contador= contador + valor

print(contador)
lista_to_string = " ".join(lista_orden)
print(lista_to_string)
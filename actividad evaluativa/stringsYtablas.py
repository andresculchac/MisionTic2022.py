'''
 es necesario que el número de columnas de A
  sea igual al número de filas de B.
'''
entrada = input()
entrada2 = input()
#separacion con x y es convertido a list
string = entrada.split("x")
separate = entrada2.split("x")
#convert to number
conv1 = [int(x) for x in string]
conv2 = [int(j) for j in separate]

#conv[1] y conv[0] sean iguales de lo contrario no se puede
if conv1[1] == conv2[0]:
    print("valido para multiplicacion de matrices")
else:
    print("Las columnas de la primera tabla deben ser iguales a las filas de la segunda tabla")





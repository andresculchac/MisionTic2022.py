from operator import truediv


def funcion_maximo(a, b):
    a = a>b
    return a
# aqui esta la funcion para saber si un numero es mayor o menor 
numero1 = int(input("ingrese el primer numero "))
numero2 = int(input("ingrese el segundo numero "))


valor = funcion_maximo(numero1, numero2)
if (valor):
    print("el numero " + str(numero1) + " es el mayor")
else:
    print("el numero " + str(numero2) + " es el mayor")

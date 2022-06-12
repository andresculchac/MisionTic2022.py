dato = 0
suma = 0
bandera = True
while (bandera or dato != 0):
    bandera = False
    dato = int(input("Ingrese un n´umero entero " + "a sumar o 0 para salir: "))
    suma += dato
    print("La suma es: " + str(suma))
requestVendedores = int(input())
vendedores = {}

# Iterar sobre cada solicitud de vendedor
for _ in range(requestVendedores):
    requestSTR = input()
    splitStr = requestSTR.split(':')
    nombre = splitStr[0]
    venta = int(splitStr[1])

    # Si el vendedor ya está en el diccionario, sumar la venta
    if nombre in vendedores:
        vendedores[nombre] += venta
    # Si no está en el diccionario, agregarlo con su venta como valor
    else:
        vendedores[nombre] = venta
    if vendedores[nombre] == 25:
        print("el ganador es", nombre)
        break





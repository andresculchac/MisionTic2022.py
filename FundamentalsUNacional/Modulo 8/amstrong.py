# Inicializar una lista para almacenar los dígitos
#Luego con esa lista
def splitNumber(numero):
    numInicial = numero
    digitos = []
    while numero > 0:
        digito = numero % 10  # Obtener el último dígito
        digitos.insert(0, digito)  # Insertar el dígito al principio de la lista, y se agrega el 0 porque se agrega al principio de la lista
        numero = numero // 10  # Eliminar el último dígito por division entera
    
    lenLista = len(digitos)
    count = 0
    for i in range(lenLista):
        algorithm = digitos[i]**lenLista
        count += algorithm
    if count != numInicial:
        return False
    return True


howManyArmStrong = int(input())

impresionFinal = list()

for i in range(howManyArmStrong):
    solicitar = int(input())
    if splitNumber(solicitar):
        impresionFinal.append(f'es ArmStrong')
    else:
        impresionFinal.append(f'no es ArmStrong') 

for nn in impresionFinal:
    print(nn)

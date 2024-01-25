#hacer una serie de fibonacci infinita


def findDivisor(num): #Encuentra los divisores de un numero
    contador = 0
    for i in range(1,num+1):
        if num%i == 0:
            contador += 1
    return contador


impresionFinal = list()

while True:
    solicitar = int(input())
    if solicitar == 0:
        break
    elif solicitar == 1:
        impresionFinal.append("Pertenece a la serie de Julianachi")
    else:
        m = 1
        for i in range(5000):
            algorithm = m + findDivisor(m)
            m = algorithm
            if m == solicitar:
                impresionFinal.append("Pertenece a la serie de Julianachi")
                break
        else:
            impresionFinal.append("No pertenece a la serie de Julianachi")

for j in impresionFinal:
    print(j)







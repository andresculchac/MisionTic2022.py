#hacer una serie de fibonacci infinita


def findDivisor(num):
    contador = 0
    for i in range(1,num+1):
        if num%i == 0:
            contador += 1
    return contador


impresionFinal = list()

flag = True
while flag:
    solicitar = int(input())
    if solicitar == 0:
        break
    else:
        m = 1
        for i in range(5000):
            algorithm = m + findDivisor(m)
            m = algorithm
            if m == solicitar:
                impresionFinal.append("Pertenece a la serie de Julianachi")
                break
        else:
            impresionFinal.append("Pertenece a la serie de Julianachi")
            break

for j in impresionFinal:
    print(j)







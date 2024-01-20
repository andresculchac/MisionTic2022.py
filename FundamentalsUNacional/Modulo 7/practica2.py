"""
El programa debe leer un número entero,
dicho número debe ser positivo y
contener una cantidad de cifras que sea par
"""

solicitar = input()
count = 0
for i in solicitar:
    count += 1



def listaUnidad(num):
    x = list()
    for i in num:
        x.append(int(i))
    return x

def firstandLast(num1):
    sumList = list()
    divide = int(len(num1)/2)
    for i in range(divide):
        algorithm = num1[i] + num1[-(i+1)]
        sumList.append(algorithm)
    return sumList

def promedio(list):
    numMajor = max(list)
    numMinor = min(list)
    redondear = round((numMajor+numMinor)/2,1)
    return redondear

if count % 2 != 0 or int(solicitar) < 0:
    print("El numero debe ser positivo y contener una cantidad par de cifras")
else:
    print(promedio(firstandLast(listaUnidad(solicitar)))) 









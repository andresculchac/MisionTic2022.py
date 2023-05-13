#lista = [3,5,2,1,4,2,2,5,1,5]
#Procedo a hacer las entradas
nMiembros = int(input())
pedirEntrada = int(input())
lista = []

for i in range(1,pedirEntrada+1):
    requestInput = int(input()) #The types of variable  can change
    addList = lista.append(requestInput)
#print(lista)
lista2 = []
N = len(lista)

for i in range(N):#algoritmo que identifique cual se repite mas, en este caso los mas ganadores
    N = len(lista)
    repitencia = lista[0]
    for j in range(1,N):
        if repitencia == lista[j]:
            lista2.append(lista[j])
    lista.remove(lista[0])

contarlista = len(lista2)
listaesperada = []
secondnumcycle = 0
contador = 0
contadorEstable = 0
primernumero = 0
segundonumero = 0

#el numero mas repetido se tiene que poner de primero 
# vamos por lo sencillo, cuantes veces se repite el 5 en la lista2
#vamos por la lista2 esperada

for i in range(contarlista):
    contarlista = len(lista2)
    firstnumcycle = lista2[0]
    for j in range(1,contarlista):
        if firstnumcycle == lista2[j]:
            contador += 1
            if lista2[j] not in listaesperada:
                listaesperada.append(lista2[j])
    if contador > contadorEstable:
        contadorEstable = contador
    elif contador < contadorEstable:
        segundonumero = firstnumcycle
    if contador > 0:
        if contador >= contadorEstable:
            primernumero = firstnumcycle
            
        contador = 0
    lista2.remove(lista2[0])
print(primernumero)
print(segundonumero)



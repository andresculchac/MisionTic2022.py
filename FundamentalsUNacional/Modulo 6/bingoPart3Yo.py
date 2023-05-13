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


print(lista2)



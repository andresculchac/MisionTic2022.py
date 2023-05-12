lista = [3,5,2,1,4,2,2,5,1,5]
contador = 0
#algoritmo que identifique cual se repite mas

#lista = [1,2,3,4,1]
lista2 = []
N = len(lista)

contador = 0
# for i in range(1,N):
#     repitencia = lista[0]
#     if  repitencia == lista[i] :
#         contador += 1
#         lista2.append(lista[i])
# lista.remove(lista[0])

for i in range(N):
    N = len(lista)
    repitencia = lista[0]
    for j in range(1,N):
        if repitencia == lista[j]:
            contador += 1
            lista2.append(lista[j])
    lista.remove(lista[0])


print(lista2)



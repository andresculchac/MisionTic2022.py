#lista = [180,175,186,179,181,173,181,170]

#ordenar por mayor y final por ciclos

#First Step

# pedirEntrada = int(input())
# ListEmpty = []

# for i in range(1,(pedirEntrada*2)+1):
#     requestInput = int(input()) #The types of variable  can change
#     addList = ListEmpty.append(requestInput)
# print(ListEmpty)

#second Step 
    #Ciclo que organiza los numeros pares e impares bien lindo

lista = [1,6,4,2,3,5]
lista2 = []
#lista esperada # [6,1,5,2,4,3]
mayor = lista[0]
menor = lista[0]
numLista = len(lista)
for i in range (1,numLista):
    if lista[i] > mayor:
        mayor = lista[i]

    if lista[i] < menor:
        menor = lista[i]
x = lista2.append(menor)
y = lista2.append(mayor)
print(lista2)
lista = [180,175,186,179,181,173,181,170]

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


lista2 = []
#lista esperada # [6,1,5,2,4,3]
mayor = lista[0]
menor = lista[0]
numLista = len(lista)

for i in range(int(numLista/2)):
    x = max(lista)
    y = min(lista)
    osea = lista2.append(x)
    verdad = lista2.append(y)
    viva =lista.remove(x)
    lau = lista.remove(y)


print(lista2)
for i in range(int(numLista/2)):
    primerpar = lista2[0]
    segundopar = lista2[1]
    if primerpar % 2 == 0 and segundopar % 2 == 0:
        v = lista2.remove(primerpar)
        vv = lista2.remove(segundopar)
        
    elif primerpar % 2 != 0 and segundopar % 2 != 0:
        v = lista2.remove(primerpar)
        vv = lista2.remove(segundopar)
    



print("Sobreviven",len(lista2),"soldados")
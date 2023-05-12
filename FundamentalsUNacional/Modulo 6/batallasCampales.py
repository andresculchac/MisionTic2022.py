pedirEntrada = int(input())
lista = []

for i in range(1,(pedirEntrada*2)+1):
    requestInput = int(input()) #The types of variable  can change
    addList = lista.append(requestInput)
#print(lista)

#second Step 
    #Ciclo que organiza los numeros pares e impares bien lindo


lista2 = []

numLista = len(lista)

for i in range(int(numLista/2)):
    x = max(lista)
    y = min(lista)
    osea = lista2.append(x)
    verdad = lista2.append(y)
    viva =lista.remove(x)
    lau = lista.remove(y)


#print(lista2)
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

#Para mi esta bien pero no encuentro el error xD, asi que me toca con un monitor.
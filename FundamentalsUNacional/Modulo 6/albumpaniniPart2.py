# x = True  #The point require find in a list the only numbers and if they repeat delete it.
# lista = []
# while x:
#     y = int(input())
#     request = lista.append(y)
#     if y == 0:
#         x = False
# lista.pop(-1)
# print(lista)

lista = [21,47,35,658,47,1,100,9,35,47] #find how many times is the number 35, and 47
listadelosrepetidos = []
writing = len(lista)
contador = 0 
contadorIdea = len(lista)
for i in range(writing):
    for j in range(writing):
        if lista[j] == lista[i]:
            contador += 1
            if contador > 1:
                x = listadelosrepetidos.append(lista[j])

    if contador == 1:
        contador = 0
    if contador > 1:
        
        contadorIdea -= 1
        contador = 0

print(contadorIdea)
print(listadelosrepetidos)
        


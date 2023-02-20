variableX = True
listaX = []

while variableX:
    variableJ = int(input())
    if variableJ == 0:
        variableX = False
    listaX.append(variableJ)
listaX.pop(-1)

#print(listaX)

# lista  = [21, 47, 35, 658, 47, 1, 100, 9, 35, 47]
# diferentes = []

conjunto = set(listaX)

lista = list(conjunto)
print(len(lista))
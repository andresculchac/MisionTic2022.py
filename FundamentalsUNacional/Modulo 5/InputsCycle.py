#This is a Input for exercises of Introduccion a la programacion

pedirEntrada = int(input())
ListEmpty = []

for i in range(1,pedirEntrada+1):
    requestInput = int(input()) #The types of variable  can change
    addList = ListEmpty.append(requestInput)
print(ListEmpty)
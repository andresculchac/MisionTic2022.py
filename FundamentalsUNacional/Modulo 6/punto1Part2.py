pedirEntrada = int(input())
ListEmpty = []
counter  = 0
for i in range(1,pedirEntrada+1):
    requestInput = int(input()) #The types of variable  can change
    if requestInput <= 5:
        addList = ListEmpty.append(requestInput)
for j in range(1,6):
    x = ListEmpty.count(j)
    print(str(j)+":",x)


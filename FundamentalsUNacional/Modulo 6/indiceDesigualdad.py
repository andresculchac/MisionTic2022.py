variableX = True
listaX = []

while variableX:
    variableJ = int(input())
    if variableJ == 0:
        variableX = False
    listaX.append(variableJ)


listaX.sort()
listaX.pop(0)
x = listaX[-3]
y = listaX[2]

operacion = x-y
op2 = (len(listaX)**2)
op3 = operacion / op2
#print(op3)
print(round(op3,2))
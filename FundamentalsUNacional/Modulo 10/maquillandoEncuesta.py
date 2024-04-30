

requestInt = int(input())
makeupGeneral = []


for i in range(requestInt): #Esto solo es la entrada fea y toca arreglarla para trabajar los datos
    makeUp = []
    requestStr = input()
    splitStr = requestStr.split(" ",3)
    for i in range(4):
        if i==0:
            continue
        elif i == 1:
            makeUp.append(int(splitStr[1]))
        elif i == 2:
            makeUp.append(splitStr[2])
        elif i == 3:
            makeUp.append(int(splitStr[3]))
    makeupGeneral.append(makeUp)

#Eliminar los negativa y los positiva reemplazar por POSITIVA
#al contrario si tiene positiva que se vaya a otra lista pon POSITIVA
#makeupGeneral = [[45, 'positiva', 7], [22, 'negativa', 6], [19, 'negativa', 9],
 #               [24, 'positiva', 10], [27, 'negativa', 9], [30, 'positiva', 10], [60, 'positiva', 7]]

newMakeUp = list() #aqui me mandaron a poner positiva en mayusculas y filtrar los percepciones positivas de negativas

for i in range(len(makeupGeneral)):
    if makeupGeneral[i][1] == "positiva": 
        makeupGeneral[i][1] = makeupGeneral[i][1].replace("positiva","POSITIVA")
        newMakeUp.append(makeupGeneral[i])
#print(newMakeUp)
#buble sort para percepcion #aqui empleo buble sort para todo
n = len(newMakeUp) #3

for i in range(n-1):
    for j in range(n-1):
        if newMakeUp[j][2]  < newMakeUp[j+1][2]:
            lump = newMakeUp[j]
            newMakeUp[j] = newMakeUp[j+1]
            newMakeUp[j+1] = lump
#buble sort para edades
print(newMakeUp)
#how many grades are there? #pero me encuentro el problema es que hay dos filtros, uno que es de el filtro va por percepciones
grades = []

for i in range(len(newMakeUp)):
    if newMakeUp[i][2] not in grades:
        grades.append(newMakeUp[i][2])

print(grades,"estas son las notas que hay")

notasDefinitivas = [] #y el otro filtro es aquel que si los dos ponen 10 se filtre por quien tiene mas edad

for i in range(len(grades)): #hacer buble sort para cada separador que haya, after unir##
    separador = []
    for j in range(n):
        if grades[i] == newMakeUp[j][2]:
            separador.append(newMakeUp[j])
    b = len(separador)
    if b == 1:
        notasDefinitivas.append(separador)
    for u in range(b-1):
        for v in range(b-1):
            if separador[v][0] < separador[v+1][0]:
                lump = separador[v]
                separador[v] = separador[v+1]
                separador[v+1] = lump
        notasDefinitivas.append(separador)

print(notasDefinitivas)

#aprendi mucho de este ejercicio, pero mas importante es que me siento feliz porque pude dominar un agoritmo de ordenamiento
#de muchas maneras




    

















            

            



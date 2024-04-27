solicitar = int(input())
talleres = [9, 11, 12,8, 12, 9, 11, 8, 11, 10, 9,10]
gradeGeneral = dict()
#gradeStudent = [555555,5,5,5,5,5,5,5,5,5,5,5,5]
for i in range(solicitar):
    requestStr = input()
    strGradeStudent = requestStr.split(',')
    gradeStudent = []
    for i in strGradeStudent:
        gradeStudent.append(int(i))

    notasRedondeadas = []
    for i in range(12):
        notas = (gradeStudent[i+1]/talleres[i])*5
        redondeo = round(notas,1)
        notasRedondeadas.append(redondeo)
    Sumatoria = sum(notasRedondeadas)/12
    redondeo2 = round(Sumatoria,1)
    gradeGeneral[gradeStudent[0]] = redondeo2
### Impresion ###
#Sorted

notasFinales = dict(sorted(gradeGeneral.items()))

# # Define tu diccionario, Itera sobre el diccionario e imprime clave: valor # #

for clave, valor in notasFinales.items():
    print(clave, valor)



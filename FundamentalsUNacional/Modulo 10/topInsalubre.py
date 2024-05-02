#insalubres = {"Rodrigo Rodriguez":[99.0, 1.75, 150.0, 240.0]}
#Peso, estatura, azucar en sangre y trigriceridos

#print(99.0/(1.75)**2)
insalubres = {}
requestExercise = int(input())

for i in range(requestExercise):
    requestStr = input()
    splitRequest = requestStr.split(',')
    listaEntera = []
    for j in range(1,len(splitRequest)):
        listaEntera.append(float(splitRequest[j]))
    insalubres[splitRequest[0]] = listaEntera

imcInsalubres = {}
#print(insalubres)

for i in insalubres:
    peso = insalubres[i][0]
    estatura = insalubres[i][1]
    imcAlgorithm = round(peso/(estatura)**2,1)
    if imcAlgorithm > 25:
        imcInsalubres[i] = imcAlgorithm

#print(imcInsalubres)
def ordenar_por_valor_y_key(item):
    return (item[1], item[0])

personasOrdenadas = dict(sorted(imcInsalubres.items(), key=ordenar_por_valor_y_key,reverse=True))

print("######################################","\n")
for key, value in personasOrdenadas.items():
    print(key, value)


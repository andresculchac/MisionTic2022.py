file = open('estudiantes.txt','r')
table = []
for renglon in file:
    datos = renglon.split(', ')
    nom = datos[0]
    ape = datos[1]
    sexo = datos[2]
    doc = int(datos[3])
    edad = int(datos[4])
    est = float(datos[5])
    prom = float(datos[6])
    estudiante = [nom, ape, sexo, doc, edad, est, prom]
    table.append(estudiante)
file.close()

table.sort(key= lambda x: x[6],reverse=True)
print('Documento\tPromedio\tNombre completo')
for e in table:
    print(e[3],e[6],e[0]+' '+e[1],sep='\t\t')

promedio, baloncesto, menores = 0,0,0
for e in table:
    promedio += e[6]
    if e[2] == "F" and e[5] >= 1.8:
        baloncesto += 1
    if e[2] == "M"  and e[5] >= 18:
        menores += 1
promedio = round(promedio/len(table),2)
print("\nPromedio general:", promedio)
print("Candidatas equipo baloncesto:", baloncesto)
print("Hombres menores de edad:", menores)

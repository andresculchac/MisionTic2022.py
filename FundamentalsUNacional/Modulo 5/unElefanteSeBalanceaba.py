weightMax = float(input())
numElefantes = float(input())
contador = 0
salida = 0
while numElefantes > 0:
    newWeight = float(input())
    #print(newWeight)
    numElefantes -= 1
    contador  = newWeight + contador
    if contador <= weightMax:
        salida += 1

print(salida)
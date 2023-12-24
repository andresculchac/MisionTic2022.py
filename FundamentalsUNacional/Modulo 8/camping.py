entrada = list()
originalEntrada = list()

ingresaNum = int(input())
for i in range(ingresaNum):
    solicitarNum = float(input())
    entrada.append(solicitarNum)
    originalEntrada.append(solicitarNum)
    

#luego de encontrar en orden los numeros encontrar en la posición original con index
n = len(entrada)
#algoritmo bubble sort
for i in range(n-1):
    for i in range(n-1):
        if entrada[i] > entrada[i+1]:
            flat = entrada[i]
            entrada[i] = entrada[i+1]
            entrada[i+1] = flat

print('Entrada mod',entrada)
print('Entrada Original', originalEntrada)

for i in range(n):
    print((originalEntrada.index(entrada[i]))+1)

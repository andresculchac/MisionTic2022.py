#La primera forma es increible la forma tan rapida que lo solucione
lista = []
parejas = []

while True:
    InfinityCastle = int(input())
    if InfinityCastle == 0:
        break
    else:
        lista.append(InfinityCastle)

cuentaLista = len(lista) #Tiene que actualizarse :)

for i in range(cuentaLista):
    cuentaLista = len(lista)
    for j in range(1,cuentaLista):
        if lista[0] + lista[j] == 1995:
            parejas.append(1)
    lista.remove(lista[0])

print(len(parejas))

            

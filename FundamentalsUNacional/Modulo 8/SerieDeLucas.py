lista = [2,1]

s = lista[0] # 2
m = lista[1] # 1

rango = 500 #hasta las primeras 500 sucesione 
topeA = 200
topeB = 300
contador = 1 #creo que toca empezar desde uno puesto que el primer arranque no esta contado como tal

for i in range(1,rango-1):

    y = s + m
    lista.append(y)
    s = y
    m = lista[i]
    if i >= topeA:
        contador += 1
        if i == contador:
            break



print(lista)
print("Contador", contador)




    

    





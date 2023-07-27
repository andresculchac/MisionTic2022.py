pedirEntrada = int(input())
lista = []
sort_lista = []
soldiers_death = 0
contador = {}


for i in range(1,(pedirEntrada*2)+1): #Esta variable es para los inputs.
    requestInput = int(input())
    addList = lista.append(requestInput)


for numero in lista: #Este for elimina los soldados repetidos y cuenta su muerte
    if numero not in contador:
        contador[numero] = 1
    else:
        contador[numero] += 1
        soldiers_death += 2
        
lista2 = [valor for valor in lista if contador[valor] <= 1]
#print(lista2)
#Este algoritmo busca encontrar el maximo valor el minimo valor
#Como tambien mirando que si son primos ambos numeros se agregar una muerte

for i in range(int(len(lista2)/2)):
    max_num = max(lista2)
    min_num = min(lista2)
    if max_num % 2 == 0 and min_num % 2 == 0 : #Estatura par
        lista2.remove(max_num)
        lista2.remove(min_num)
        soldiers_death += 2
    elif max_num % 2 != 0 and min_num % 2 != 0: #Estatura impar
        lista2.remove(max_num)
        lista2.remove(min_num)
        soldiers_death += 2
    else:
        lista2.remove(max_num)
        lista2.remove(min_num)


print(f'Sobreviven {len(lista)-soldiers_death} soldados')

#Estoy mal y no es porque este mal el algoritmo porque lo desarrolle en como lo pense
#Pero mainterprete el codigo porque iba por equipos es por eso que nunca pude desarrollar correctamente el ejercicio
#Con el codigo de prueba


#2
# 170
# 175
# 180
# 165




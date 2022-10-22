miLista = []
contadorPa1=0
contadorPa2=0
contadorPa3=0
contadorPa4=0
contadorPa5=0

n = int(input()) #elemento que identifica cuantos numeros se van a poner 
for _ in range(n):
    elemento = int(input())
    miLista.append(elemento)


for i in miLista:  #for que lee pues la lista y con esto empiezo a identificar donde estan  los numeros del 1 al 5
    #contadores del 1 no mas
    if i == 1:
        contadorPa1 += 1
    elif i == 2:
        contadorPa2 += 1
    elif i == 3:
        contadorPa3 += 1
    elif i == 4:
        contadorPa4 += 1
    elif i == 5:
        contadorPa5 += 1
        
print("1:",contadorPa1)
print("2:",contadorPa2)
print("3:",contadorPa3)
print("4:",contadorPa4)
print("5:",contadorPa5)

#haciendo el tipo de impresion que tiene la plataforma 

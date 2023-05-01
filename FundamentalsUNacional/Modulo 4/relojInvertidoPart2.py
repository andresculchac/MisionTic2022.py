#Fallo con la hora 12:25 

horas,minutos = int(input()),int(input())
horasEstables = 11
minutosEstables = 60
#Algoritmo base
algoritmoHoras = horasEstables-horas
algoritmoMinutos = minutosEstables-minutos
# Algoritmo detalles 
if algoritmoMinutos == 60: #mod para horas 3,6,9,12
    algoritmoMinutos = 0
    if algoritmoHoras == -1:
        algoritmoHoras = 11
    print(str(algoritmoHoras+1)+":"+str(algoritmoMinutos))
# elif algoritmoHoras == 0 or algoritmoHoras == -1: #Este problema solucion las 11:30 entonces el error aqui es que da 0 la suma
#     # y por el otro, el error del -1 pues no da la resta bien

elif algoritmoHoras ==  0 or algoritmoHoras == 1:
    algoritmoHoras = 12
    print(str(algoritmoHoras)+":"+str(algoritmoMinutos))

elif algoritmoHoras == -1: #Con esa variable no estoy conforme siento que si busco la manera podemos integrarla mejor
    algoritmoHoras = 11#No estoy conforme con esta porque es una modificacion cuando ya cree un arreglo para las 12
    print(str(algoritmoHoras)+":"+str(algoritmoMinutos))
else:
    print(str(algoritmoHoras)+":"+str(algoritmoMinutos))


horas,minutos = int(input()),int(input())
horasEstables = 11
minutosEstables = 60
#Algoritmo base
algoritmoHoras = horasEstables-horas
algoritmoMinutos = minutosEstables-minutos
#Algoritmo detalles 
if algoritmoMinutos == 60: #mod para horas 3,6,9,12
    algoritmoHoras +=1
    if algoritmoHoras == 0:
        algoritmoHoras = 12
    algoritmoMinutos = 0
    print(str(algoritmoHoras)+":"+str(algoritmoMinutos))
elif algoritmoHoras == 0: #arreglo el problema de las 12
    algoritmoHoras = 12
    print(str(algoritmoHoras)+":"+str(algoritmoMinutos))
elif algoritmoHoras == -1: #Con esa variable no estoy conforme siento que si busco la manera podemos integrarla mejor
    #No estoy conforme con esta porque es una modificacion cuando ya cree un arreglo para las 12
    print(str(algoritmoHoras*(-1))+":"+str(algoritmoMinutos))
else:
    print(str(algoritmoHoras)+":"+str(algoritmoMinutos))
#impresion

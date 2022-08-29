#Multiplo de 13 
#Solo trabajo con multiplo de 13

numCalle = int(input())
numCasa = int(input())

if numCalle%13 == 0:
    if numCasa%13 == 0:
        print("La direccion calle",numCalle,"#",numCasa,"esta prohibida")
elif numCalle%13 != 0:
    if numCasa%13 != 0:
        print("La direccion calle",numCalle,"#",numCasa,"no esta prohibida")



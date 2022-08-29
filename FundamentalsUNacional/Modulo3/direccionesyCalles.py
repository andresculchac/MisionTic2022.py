#Multiplo de 13 
#Solo trabajo con multiplo de 13
#Multiplos de 23
numCalle = int(input())
numCasa = int(input())

if numCalle%13 or numCalle%23:
    print("La direccion calle",numCalle,"#",numCasa,"esta prohibida")

elif numCasa%13 or numCasa%23:
    print("La direccion calle",numCasa,"#",numCalle,"esta prohibida")

else:
    print("La direccion calle",numCalle,"#",numCasa,"no esta prohibida")


   
#hola xd 
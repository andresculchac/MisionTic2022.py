#Multiplo de 13 
#Solo trabajo con multiplo de 13
#Multiplos de 23
numCalle = int(input())
numCasa = int(input())

if numCalle%13 ==0 or numCalle%23 ==0:
    print("La direccion calle",numCalle,"#",numCasa,"esta prohibida ")

elif numCasa%13 ==0 or numCasa%23 ==0:
    print("La direccion calle",numCalle,"#",numCasa,"esta prohibida")

else:
    print("La direccion calle",numCalle,"#",numCasa,"no esta prohibida")


   
#hola xd 
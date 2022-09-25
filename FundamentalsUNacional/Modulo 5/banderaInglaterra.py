ancho = int(input())
altura = int(input())
mitad = altura /2 +0.5
mitadAncho = ancho /2 +0.5
if (ancho%2 != 0 and altura%2 != 0) < 20:
    #son primos y menores a 20
    
    for i in range(1,altura+1):  #mejor hacer un algorithm que cuando llegue la mediana se ponga una "0" despues que lo logremos solo es duplicar

        if i == mitad:
            i = "0"
        else:
            i = "X"
        print(i)
    print("\n")
    
        
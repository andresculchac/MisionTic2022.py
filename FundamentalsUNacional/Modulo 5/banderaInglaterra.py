ancho = int(input())
altura = int(input())
mitad = altura/2+0.5
mitadAncho = ancho /2 +0.5
if (ancho%2 != 0 and altura%2 != 0) < 20:
    #son primos y menores a 20
    for j in range(1,altura+1):
        j = "+"
    for i in range(1,altura+1):
        if i == mitad:
            i = "+"
        else:
            i = "0"
        print(str(i)*int(mitadAncho-1)+str(j)+str(i)*int(mitadAncho-1))
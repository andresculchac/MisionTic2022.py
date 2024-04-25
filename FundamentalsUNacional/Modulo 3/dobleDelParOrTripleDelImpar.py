#logica en whiteboard


num1 = int(input())
residuo = num1%2   #saca el residuo de un numero y si da 0 es par si no es impar 


if residuo == 0:
    print(2*num1)
elif residuo == 1:
    print(3*num1)

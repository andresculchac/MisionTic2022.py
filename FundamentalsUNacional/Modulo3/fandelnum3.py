num1 = int(input())

if num1 == 3:
    print("El numero 3 es el mejor")

elif num1 % 3 == 0:
    print("El numero",num1,"es multiplo de 3. Y el numero 3 es el mejor")

elif num1 != 0:
    if (num1 + 1)%3 == 0:
        print("El numero" ,num1, "no es multiplo de 3, pero si le sumas 1 el resultado si lo es. Y el numero 3 es el mejor")
    if (num1 - 1)%3 == 0:
        print('El numero',num1, 'no es multiplo de 3, pero si le restas 1 el resultado si lo es. Y el numero 3 es el mejor')

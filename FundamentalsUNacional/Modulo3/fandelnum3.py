starUpnum = int(input())

if starUpnum == 3:
    print("El numero 3 es el mejor")

elif starUpnum % 3 == 0:
    print("El numero",starUpnum,"es multiplo de 3. Y el numero 3 es el mejor")

elif starUpnum != 0:
    if (starUpnum + 1)%3 == 0:
        print("El numero" ,starUpnum, "no es multiplo de 3, pero si le sumas 1 el resultado si lo es. Y el numero 3 es el mejor")
    if (starUpnum - 1)%3 == 0:
        print('El numero',starUpnum, 'no es multiplo de 3, pero si le restas 1 el resultado si lo es. Y el numero 3 es el mejor')

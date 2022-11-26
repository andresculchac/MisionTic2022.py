'''
Esta es la entrada estimado profesor
'''
entrada = input()
entrada2 = input()
x = []
u = []

#Separacion de string mediante la fun(split())
string = entrada.split("x")
separate = entrada2.split("x")

#Entradas str a int
conv1 = [int(x) for x in string]
conv2 = [int(j) for j in separate]

#Condicional num columnas A == Num filas B
if conv1[1] == conv2[0]: 
    listaapendice =     []
    listaapendice2 =    []
    listaapendice3 =    []
    listaapendice4 =    []

    #Matriz x
    for _ in range(conv1[0]):
        xy = int(input())
        aaa = listaapendice.append(xy)
    x.append(listaapendice)
    for _ in range(conv1[1]):
        xy = int(input())
        aaa = listaapendice2.append(xy)
    x.append(listaapendice2)

    #matriz u
    for _ in range(conv2[1]):
        xy = int(input())
        aaa = listaapendice3.append(xy)
    u.append(listaapendice3)
    for _ in range(conv2[1]):
        xy = int(input())
        aaa = listaapendice4.append(xy)
    u.append(listaapendice4)

    #Listax,ListaY Almacenamiento Y ejecucion de Multiplicas Matrices
    listax = []
    listay = []
    v = len(u[0])
    for i in range(len(x)):
        for j in range(v):
            z = x[i][0] * u[0][j]
            listax.append(z)
    print(listax)

    l = len(u[0])
    for i in range(len(u)):
        for v in range(l):
            m = x[i][1] * u[1][v]
            listay.append(m)
    print(listay)
    #este es el que suma y de una vez saca la lista xd
    #
    sumList = len(listax)
    for i in range(sumList):
        print(listax[i]+listay[i],end=" ")
    print("")

    for i in range(conv1[0]):       #filas
        for j in range(conv2[1]):   #columnas
            print(listax[i]+listay[i],end=" ")
        print("")

    

else:
    print("Las columnas de la primera tabla deben ser iguales a las filas de la segunda tabla")





'''
Esta es la entrada estimado profesor
'''
entrada = input()
entrada2 = input()
x = []
u = []

#separacion con x y es convertido a list
string = entrada.split("x")
separate = entrada2.split("x")

conv1 = [int(x) for x in string]
conv2 = [int(j) for j in separate]
if conv1[1] == conv2[0]:
    #Pedir numeros comenzando por las filas
    numinput = conv1[0]*conv1[1] #si seria 2*2 seria 4 numeros que pide
    numinput2 = conv2[0]*conv2[1] #digameos 2*3 seria 6 numeros de a dos listas
    suminputs = numinput + numinput2
    listaapendice = []
    listaapendice2 = []
    listaapendice3 = []
    listaapendice4 = []
    for _ in range(conv1[0]): #tengo que generar l listas
        xy = int(input())
        aaa = listaapendice.append(xy)
    x.append(listaapendice)
    for _ in range(conv1[1]): #tengo que generar l listas
        xy = int(input())
        aaa = listaapendice2.append(xy)
    x.append(listaapendice2)
    #matriz 2
    for _ in range(conv2[0]): #tengo que generar l listas
        xy = int(input())
        aaa = listaapendice3.append(xy)
    u.append(listaapendice3)
    for _ in range(conv2[1]): #tengo que generar l listas
        xy = int(input())
        aaa = listaapendice4.append(xy)
    u.append(listaapendice4)
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
        print(listax[i]+listay[i],end="\n")

    

else:
    print("Las columnas de la primera tabla deben ser iguales a las filas de la segunda tabla")





'''
Esta es la entrada estimado profesor
'''
inputPrincipal = []
InputPrincipal2 = []
entrada = input()
entrada2 = input()

birl = []
birl2 = []

ul = []
uj = []


u = []

#Separacion de string mediante la fun(split())
string = entrada.split('x')
separate = entrada2.split('x')
list1 = int(string[0])
list2 = int(string[1])
list3 = int(separate[0])
list4 = int(separate[1])
num_m1 =list1*list2
num_m2 = list3*list4

#Entradas str a int
conv1 = [int(x) for x in string]
conv2 = [int(j) for j in separate]

#Encontrar el maximo para las listas
maxX = max(conv1[0],conv1[1])
maxU = max(conv2[0],conv2[1])

#Condicional num columnas A == Num filas B
if conv1[1] == conv2[0]: 
    for j in range(num_m1):
        m1 = int(input())      
        birl.append(m1)   
        if len(birl) == list2:
            inputPrincipal.append(birl)
            birl = []
    for j in range(num_m2):
        m2 = int(input())
        birl2.append(m2)
        if len(birl2) == list4:
            InputPrincipal2.append(birl2)
            birl2 = []

    #Listax,ListaY Almacenamiento Y ejecucion de Multiplicas Matrices
    listax = []
    listay = []
    v = len(InputPrincipal2[0])
    for i in range(len(inputPrincipal)):
        for j in range(v):
            z = inputPrincipal[i][0] * InputPrincipal2[0][j]
            listainputPrincipal.append(z)
    print(listainputPrincipal)

    l = len(InputPrincipal2[0])
    for i in range(len(InputPrincipal2)):
        for v in range(l):
            m = inputPrincipal[i][1] * InputPrincipal2[1][v]
            listay.append(m)
    print(listay)
    #este es el que suma y de una vez saca la lista inputPrincipald
    #
    sumList = len(listainputPrincipal)
    for i in range(sumList):
        print(listainputPrincipal[i]+listay[i],end=" ")
    print("")
    contador = 0
    # for i in range(conv1[0]):       #filas
    #     for j in range(conv2[1]):   #columnas
    #         print(listainputPrincipal[i]+listay[i],end=" ")
    #     print("")
    for i in range(conv1[0]):       #filas
        for j in range(conv2[1]): #columnas  
            print(listainputPrincipal[contador]+listay[contador],end=" ")
            contador += 1
        print("")

    

else:
    print("Las columnas de la primera tabla deben ser iguales a las filas de la segunda tabla")





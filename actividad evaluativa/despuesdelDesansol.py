# for i in range(2): #filas
#     for j in range(3): #columnas
#         print(0,end=' ')
#     print("")
conv1 = [2,2]
conv2 = [2,3]

listax = [5,4,1,-3]
listay = [14,16,28,32]
contador = 0
#Primero se desarrollan las 
for i in range(conv1[0]):       #filas
        for j in range(conv2[1]): #columnas  
            print(listax[contador]+listay[contador],end=" ")
            contador += 1
        print("")

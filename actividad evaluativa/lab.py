#Estimado profesor aqui puede ver que el codigo ya esta adaptado
#para ponerlo a cualquier lista solo me falta el tiempo para la entrada

x = [[5,4],[1,-3]]
u = [[8,4,0],[-1,6,7]]

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
    print(listax[i]+listay[i])



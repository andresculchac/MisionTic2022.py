# a=['1','2','3','4']

# b= [int(x) for x in a]

# print(b)

x = [[5,4],[1,-3]]
u = [[8,4,0],[-1,6,7]]

listax = []
listay = []
v = len(u[0])
for i in range(v):
    z = x[0][0] * u[0][i]
    listax.append(z)
print(listax)
l = len(u[0])
for i in range(l):
    m = x[0][1] * u[1][i]
    listay.append(m)
print(listay)
#este es el que suma y de una vez saca la lista xd
#
sumList = len(listax)
for i in range(sumList):
    print(listax[i]+listay[i]).join()
# print(u[0][0])
#multiplicacionsinfor = 
#print(x[0][0])
# contadoraja = 0
# for i in u:
#     print(x[0][contadoraja] * i[0])
#     contadoraja += 1

# for j in range(len(u)):
#     for i in u:
#         print(x[0][j] * i[0])
#     # print(x[0][j] * j[0])


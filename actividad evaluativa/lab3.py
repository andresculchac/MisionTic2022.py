l = [2,3]
l1 = [3,2]


listglobal = []
listax = []
multiplicacion = l[1] * l[0]
multiplil1 = l1[1] * l[0]
for j in range(multiplicacion):
    pedir = input
    pedir = int(input())

    listax.append(pedir)
    if len(listax) == l[1]:
        listglobal.append(listax)
        




print(listglobal)
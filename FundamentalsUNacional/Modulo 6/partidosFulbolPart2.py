pedirEntrada = int(input())
realMadrid = []
fcBarcelona = []
ptsMadrid = 0
ptsBarcelona = 0

for j in range(2):
    if j == 0: #Input for FcBarcelona
        for i in range(1,(pedirEntrada+1)):
            requestInput = int(input())
            addList = fcBarcelona.append(requestInput)

    if j == 1: #Input for RealMadrid
        for i in range(1,(pedirEntrada+1)):
            requestInput = int(input())
            addList = realMadrid.append(requestInput)
            
#Give point to they winners

for y in range(pedirEntrada):
    if realMadrid[y]==fcBarcelona[y]:
        ptsMadrid += 1
        ptsBarcelona += 1
    elif realMadrid[y]>fcBarcelona[y]:
        ptsMadrid += 2
    else:
        ptsBarcelona +=2

print("Ballenota Futbol Club:",ptsBarcelona)
print("Real Mandril:",ptsMadrid)
with open('mensaje.txt','r') as file:
    chainStr = []
    for linea in file:
        removeSpace = linea.strip()
        chainStr.append(removeSpace)

storageRoom = []

for cadenas in chainStr:
    twoChains = ''
    long    =   len(cadenas)
    for i in range(long-1,-1,-1):
        twoChains   +=  cadenas[i]
    storageRoom.append(twoChains)

for unloading in storageRoom:
    print(unloading)

        

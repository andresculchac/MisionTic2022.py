def portales(port:list,rick,morty):
    if rick == 'C-137': return morty
    for galaxy in port:
        if galaxy[0] == rick: return portales(port,galaxy[1],morty+1)
    return -1
for yellow_port in range(int(input())):
    rick,port = None, []
    for didier in range(int(input())):
        if rick == None: rick = input().split()[1]
        else: port.append(input().split())
    xxy = portales(port,rick,1)
    green = f'Pueden volver rick C-137 en {xxy} saltos' if xxy!= -1 else 'Deambulan por el multiverso'
    print(green)
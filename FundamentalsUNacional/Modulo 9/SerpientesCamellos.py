Solicitar = int(input())
entrega = []
for x in range(Solicitar):
    requestStr = input()
    splitStr = requestStr.split('_')
    camello = ""
    for i in splitStr:
        upperStr = i.capitalize()
        camello += upperStr
    entrega.append(camello)

for i in entrega:
    print(i)
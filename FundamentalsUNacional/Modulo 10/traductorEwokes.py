requestWords = int(input())

dictEwokes = dict()
for j in range(requestWords):
    requestStr = input()
    splitStr = requestStr.split(' ')
    for i in range(len(splitStr)):
        dictEwokes[splitStr[0]] =   splitStr[1]

requestEwokes   =   int(input())
printOuput= []
for _ in range(requestEwokes):
    request2 = input()
    if request2 in dictEwokes:
        printOuput.append(dictEwokes[request2])
    else:
        printOuput.append("palabra no encontrada")

for _ in printOuput:
    print(_)
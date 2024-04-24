#Example testing
solicitar = int(input())
response = []
#Objetive ["MF", "FF", "MM"], i take two letters
for i in range(solicitar):
    testing = input()
    splitStr= testing.split(" ")
    CountM = 0
    CountF = 0
    for i in range(len(splitStr)):
        for j in splitStr[i]:
            identify = ord(j)
            if identify == 77:
                CountM += 1
            else:
                CountF += 1
    if CountF == CountM:
        response.append("Es posible hacer un unico circulo")
    else:
        response.append("No es posible")

for i in response:
    print(i)

#Primero la entrada 
requestInt = int(input())
printOuput = []
months = {"marzo":3,"abril":4,"mayo":5,"junio":6,"julio":7,"agosto":8,
     "septiembre":9,"octubre":10,"noviembre":11,"diciembre":12,"enero":13,"febrero":14}
days = {0:"sabado",1:"domingo",2:"lunes",3:"martes",4:"miercoles",
        5:"jueves",6:"viernes"}

for _ in range(requestInt):
    Exm = input()

    d = 0
    m = ""
    y = 0

    splitStr = Exm.split('-')
    for i in range(len(splitStr)):
        if i == 0:
            d = int(splitStr[i])
        elif i == 1:
            m = splitStr[i]
        else:
            if m == "enero" or m == "febrero":
                y = int(splitStr[i])-1
            else:
                y = int(splitStr[i])


    formula = (d + ((13*(months[m]+1)//5)  + y + (y//4) - (y//100) + (y//400)))%7

    printOuput.append(days[int(formula)])

for _ in printOuput:
    print(_)
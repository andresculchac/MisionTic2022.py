simpleNum = float(input())
quackity = float(input())
num3 = float(input())

#3.0 5.0 4.0
if simpleNum <quackity and quackity > num3 and num3> simpleNum:
    print(num3,"es la mediana")
#3 1 2
elif simpleNum > quackity and quackity < num3 and num3<simpleNum:
    print(num3,"es la mediana")
#3.0 4.0 5.0 ejemplo para que de la mediana
elif simpleNum <quackity and quackity < num3 and num3 > simpleNum:
    print(quackity,"es la mediana")
# 5.0 3.0 1.0 ejemplo para esta 
elif simpleNum > quackity and quackity > num3 and num3 < simpleNum:
    print(simpleNum, "es la mediana")
#10 20 20
elif simpleNum < quackity and quackity == num3 and num3 > simpleNum:
    print(quackity ,"es la mediana")
#20 20 10
elif simpleNum ==  quackity and quackity > num3 and num3 < simpleNum:
    print(quackity,"es la mediana")
# 70 10 80
elif simpleNum > quackity and quackity < num3 and num3 > simpleNum:
    print(simpleNum,"es la mediana")
# 444.44 555.55 333.33
elif simpleNum < quackity and quackity > num3 and num3 < simpleNum:
    print(simpleNum,"es la mediana")
if simpleNum > quackity and quackity < num3 and num3 == simpleNum:
    print(simpleNum,"es la mediana")
if simpleNum == quackity and quackity == num3  and num3 == simpleNum:
    print(simpleNum,"es la mediana")

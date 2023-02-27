valuehour = int(input())
valueAlso = int(input())

if valueAlso >= 46:
    horasExtras = (valueAlso - 45)*(valuehour*(150/100))
    salario = valuehour * 45
    print("$",int(horasExtras) + salario)
else:
    print("$",valueAlso * valuehour)

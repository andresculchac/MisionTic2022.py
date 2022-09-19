valorHora = int(input())
valorExtra = int(input())

if valorExtra >= 46:
    horasExtras = (valorExtra - 45)*(valorHora*(150/100))
    salario = valorHora * 45
    print("$",int(horasExtras) + salario)
else:
    print("$",valorExtra * valorHora)

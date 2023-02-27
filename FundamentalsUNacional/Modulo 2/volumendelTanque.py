r,h,v,m = float(input()),float(input()),float(input()),float(input())
pi = 3.14159
formula = pi*(r**2)*h
vaciado = v*m
resultadoFinal = (formula-vaciado)
formulaFinal =(round(resultadoFinal,3))
if formulaFinal>0:
    print(formulaFinal)
else:
    print(0)
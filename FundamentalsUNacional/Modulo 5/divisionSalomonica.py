variableCambiante = float(input())
contador = 0

while variableCambiante > 1:
    divisor = variableCambiante /2
    variableCambiante = divisor 
    contador += 1
    if variableCambiante < 10:
        #esta es la que se queda el juzgado
        variableCambiante = 0
        #print(variableCambiante)
print(contador)
import math
#Preguntar como ¿Cómo usar FUNCIONES como ARGUMENTOS en OTRAS FUNCIONES?
#Por ahora mi objetivo es ponerme al dia con esto
ListaFinal  = []

def factorLorenz (f):
    metroS = ((f*1000)/3600)**2 #De Km a metros por segundo
    lorenz = 1/math.sqrt(1-(metroS/(299792458**2)))
    redondear = round(lorenz,15)
    
    return redondear

NumerosEntrantes = int(input())
for i in range(NumerosEntrantes):
    entreNum = float(input())
    NewFactor = factorLorenz(entreNum)
    ListaFinal.append(NewFactor)
for i in ListaFinal:
    print(i)

#Este ejercicio se pudo haber desarrllado desde Inputcycle y a partir de ahi la funcion opera
    


numLotes = float(input())
numChiki = float(input())
incrementoChiki =float(input())

contadorM2 = 0

while numLotes > 0:
    exponencia = numChiki **2
    contadorM2 += exponencia
    incremento = numChiki + incrementoChiki
    numChiki = incremento
    numLotes -= 1
print("El area total es de",contadorM2,"metros cuadrados")

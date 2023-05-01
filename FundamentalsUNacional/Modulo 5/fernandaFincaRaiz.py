
andresc = float(input())
chapid = float(input())
incrementoChiki =float(input())

contadorM2 = 0

while andresc > 0:
    exponencia = chapid **2
    contadorM2 += exponencia
    incremento = chapid + incrementoChiki
    chapid = incremento
    andresc -= 1
print("El area total es de",contadorM2,"metros cuadrados")

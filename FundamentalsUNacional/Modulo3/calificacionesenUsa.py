simpleLetter = float(input())
if simpleLetter >= 90:
    print("El porcentaje",simpleLetter,"corresponde a la calificacion A")
elif simpleLetter >= 80 and simpleLetter < 90:
    print("El porcentaje",simpleLetter,"corresponde a la calificacion B")
elif simpleLetter >= 70 and simpleLetter < 80:
    print("El porcentaje",simpleLetter,"corresponde a la calificacion C")
    #print("El porcentaje 70.0 corresponde a la calificacion E")
elif simpleLetter >= 60 and simpleLetter < 70:
    print("El porcentaje",simpleLetter,"corresponde a la calificacion D")
elif simpleLetter >= 40 and simpleLetter < 60:
    print("El porcentaje",simpleLetter,"corresponde a la calificacion E")
else:
    print("El porcentaje",simpleLetter,"corresponde a la calificacion F")
    #print("El porcentaje 70.0 corresponde a la calificacion E")

letterUsa = float(input())
if letterUsa >= 90:
    print("El porcentaje",letterUsa,"corresponde a la calificacion A")
elif letterUsa >= 80 and letterUsa < 90:
    print("El porcentaje",letterUsa,"corresponde a la calificacion B")
elif letterUsa >= 70 and letterUsa < 80:
    print("El porcentaje",letterUsa,"corresponde a la calificacion E")
    #print("El porcentaje 70.0 corresponde a la calificacion E")
elif letterUsa >= 60 and letterUsa < 70:
    print("El porcentaje",letterUsa,"corresponde a la calificacion D")
elif letterUsa >= 40 and letterUsa < 60:
    print("El porcentaje",letterUsa,"corresponde a la calificacion E")
else:
    print("El porcentaje",letterUsa,"corresponde a la calificacion F")
    print("El porcentaje 70.0 corresponde a la calificacion E")

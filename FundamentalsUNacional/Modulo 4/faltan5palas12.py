horas = int(input())
minutos = int(input())
tiempo = input()

#algorithm that you tell how much left for new yearly

if tiempo == "pm": #midday
    if horas ==12:
        midday = ((horas*60)-minutos)
        print("Faltan",midday,"para las 12")
        
    if horas != 12:
        hourTominutes = horas * 60
        midnight = 720
        plusMinutes = hourTominutes + minutos
        faltantes = midnight - plusMinutes
        print("Faltan",faltantes,"para las 12")

if tiempo =="am": 
    if horas ==12:
        newAmaneciendo=(24*60)-minutos
        print("Faltan",newAmaneciendo,"para las 12")
    if horas != 12:
        horasRestantes = ((24-horas)*60)-minutos
        print("Faltan",horasRestantes,"para las 12")

hours = int(input())
minutes = int(input())
time = input()

#algorithm that you tell how much left for new yearly andres culchac chapid 

if time == "pm": #midday
    if hours ==12:
        midday = ((hours*60)-minutes)
        print("Faltan",midday,"para las 12")
        
    if hours != 12:
        hourTominutes = hours * 60
        midnight = 720
        plusMinutes = hourTominutes + minutes
        faltantes = midnight - plusMinutes
        print("Faltan",faltantes,"para las 12")

if time =="am": 
    if hours ==12:
        newAmaneciendo=(24*60)-minutes
        print("Faltan",newAmaneciendo,"para las 12")
    if hours != 12:
        hoursRestantes = ((24-hours)*60)-minutes
        print("Faltan",hoursRestantes,"para las 12")

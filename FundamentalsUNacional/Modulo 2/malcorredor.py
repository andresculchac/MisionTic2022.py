Inicio = float(input())
horas = ((Inicio/60)/60)
obtHoras = int(horas)
Minutos = (horas-obtHoras)*60
obtMinutos =(int(Minutos))
segundos = (Minutos-obtMinutos)*60
obtSegundos = (round(segundos))



final = print(str(obtHoras)+":"+str(obtMinutos)+":"+str(obtSegundos))



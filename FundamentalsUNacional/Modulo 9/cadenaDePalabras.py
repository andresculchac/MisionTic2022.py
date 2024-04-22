cadenaRota = ["raza", "zapato", "toronja", "jazmin", "minuta", "tapa", "aparato"]


bandera = True
for i in range(1,len(cadenaRota)):
    lastTwo = cadenaRota[i-1][-2:]
    letraEvaluada = cadenaRota[i][:2]
    lastTree = cadenaRota[i-1][-3:]
    letraEvuluadaTree = cadenaRota[i][:3]

    if (lastTwo == letraEvaluada) or (lastTree == letraEvuluadaTree):
        bandera = True
    else:
        bandera = False
        break

if bandera:
    print("cadena completa")
else:
    print("cadena rota")

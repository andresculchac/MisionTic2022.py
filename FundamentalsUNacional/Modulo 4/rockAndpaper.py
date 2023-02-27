andresPlayer = input()
julianSapo = input()

if andresPlayer == julianSapo:
    print("empate")

elif andresPlayer == "tijera" and julianSapo == "papel": 
    print("tijera vence papel")   
elif andresPlayer == "papel" and julianSapo == "tijera":
    print("tijera vence papel")
elif andresPlayer == "papel" and julianSapo == "tijera ": #este va con espacio en tijera por el problema de la platform
    print("tijera vence papel")

elif andresPlayer == "papel" and julianSapo == "piedra":
    print("papel vence piedra")
elif andresPlayer == "piedra" and julianSapo == "papel":
    print("papel vence piedra")

elif andresPlayer == "piedra" and julianSapo == "tijera":
    print("piedra vence tijera")
elif andresPlayer == "tijera" and julianSapo == "piedra":
    print("piedra vence tijera")
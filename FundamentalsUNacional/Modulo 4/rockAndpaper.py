playerNum1 = input()
playerNum2 = input()

if playerNum1 == playerNum2:
    print("empate")

elif playerNum1 == "tijera" and playerNum2 == "papel": 
    print("tijera vence papel")   
elif playerNum1 == "papel" and playerNum2 == "tijera":
    print("tijera vence papel")
elif playerNum1 == "papel" and playerNum2 == "tijera ": #este va con espacio en tijera por el problema de la platform
    print("tijera vence papel")

elif playerNum1 == "papel" and playerNum2 == "piedra":
    print("papel vence piedra")
elif playerNum1 == "piedra" and playerNum2 == "papel":
    print("papel vence piedra")

elif playerNum1 == "piedra" and playerNum2 == "tijera":
    print("piedra vence tijera")
elif playerNum1 == "tijera" and playerNum2 == "piedra":
    print("piedra vence tijera")
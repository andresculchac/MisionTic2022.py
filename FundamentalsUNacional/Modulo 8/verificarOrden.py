
def orden(lista):
    for i in range(len(lista)):
        if lista[0] + i == lista[i]:
            if lista[0] +1 != lista[1]:
                return False          
        else:
            return False
            break
    return True
def letrasIgual(listongus):
    for i in listongus:
        if listongus[0] != i:
            return False
    return True

impresionFinal = list()


pedirNumManos = int(input())
for j in range(pedirNumManos):
    NumCartas = list()
    letrasManos = list()
    for i in range(5):
        SolicitarNumCartas   = int(input())
        SolicitarletrasManos = input()
        letrasManos.append(SolicitarletrasManos)
        NumCartas.append(SolicitarNumCartas)

    #ordenarLista
    OrdenarLista = sorted(NumCartas)

    if orden(OrdenarLista) and OrdenarLista[0] == 10 and OrdenarLista[4] == 14 and letrasIgual(letrasManos):
        realxD=f"Escalera Real"
        impresionFinal.append(realxD)
    elif orden(OrdenarLista) and letrasIgual(letrasManos):
        ColorRealxD=f"Escalera Color"
        impresionFinal.append(ColorRealxD)
    elif letrasIgual(letrasManos) and not orden(OrdenarLista):
        ColorxD=f"Color"
        impresionFinal.append(ColorxD)
    else:
        x=f"Escalera Normal"
        impresionFinal.append(x)   

for m in impresionFinal:
    print(m)
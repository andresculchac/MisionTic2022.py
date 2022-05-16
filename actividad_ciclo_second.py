# empezamos numerando las variables


cadena_pedro = input().upper()
cadena_nestor = input().upper()
cadena_jurado = input().upper()
sumatoria_para_pedro = 0     #LO DE AQUI VAN A SER LAS SUMATORIAS 
sumatoria_para_nestor = 0


# Lo que deberiamos hacer es hacer como una cadena que analice a todos de una vez
# pero tambien como un contador que diga que si tiene un punto se imprima otro punto pero no se como dibujarlo
# tambien esta hallar el problema del jurado y dependiendo de el numero de sus letras hacer el programa 

def primeraletra ():
    for letras in cadena_jurado:
        if cadena_jurado[0] in cadena_pedro:
            print("punto para pedro J")
            sumatoria_para_pedro += 1
            break
        
        elif cadena_jurado[0] in cadena_nestor:
            print("punto para nestor K")
            sumatoria_para_nestor += 1
            break        
    else:
        print("L")
        
primeraletra()

for letras in cadena_jurado:   
    if cadena_jurado[1] in cadena_pedro[1]:
        print("punto para pedro vale huevo porque maldita sea  ")
        sumatoria_para_pedro + 2
        break 
    elif cadena_jurado[1] in cadena_nestor[1]:
        print("punto para nestor ")
        sumatoria_para_nestor + 2
        break
    elif sumatoria_para_pedro == 1:
        print("J")
        break
    elif sumatoria_para_nestor == 1:
        print("J")
        break
else:
    print("L")


    
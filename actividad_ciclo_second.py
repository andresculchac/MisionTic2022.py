# empezamos numerando las variables


cadena_pedro = input()
cadena_nestor = input()
cadena_jurado = input()
sumatoria_para_pedro = 0     
sumatoria_para_nestor = 0


# Lo que deberiamos hacer es hacer como una cadena que analice a todos de una vez
# pero tambien como un contador que diga que si tiene un punto se imprima otro punto pero no se como dibujarlo
# tambien esta hallar el problema del jurado y dependiendo de el numero de sus letras hacer el programa 

for inicial in cadena_jurado:
    if inicial in cadena_pedro:
        sumatoria_para_pedro += 1
    if inicial in cadena_nestor:
        sumatoria_para_nestor += 1
        # hasta aqui parece que esta bien lo qe falta son las impresiones
    if sumatoria_para_pedro > sumatoria_para_nestor:
        print("j", end="")
    elif sumatoria_para_pedro < sumatoria_para_nestor:
        print("K", end="")
    if sumatoria_para_nestor == sumatoria_para_pedro:
        print("L", end="")

print(end="")













    
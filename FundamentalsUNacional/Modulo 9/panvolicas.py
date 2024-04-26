impresion = []
entrada = int(input())


for x in range(entrada):
    requestStr = input()
    dict = {"a":0,"e":0,"i":0,"o":0,"u":0}
    for i in requestStr:        
        if i in dict:
            dict[i] += 1
    flag = True
    for i in dict.values():
        if i == 0:
            flag = False
            break #Este tipo de break sirve para casos general, diferenciando de la monja y el jamon
    if flag == True:
        impresion.append("Panvolica")
    else:
        impresion.append("No es panvolica")


for i in impresion:
    print(i)
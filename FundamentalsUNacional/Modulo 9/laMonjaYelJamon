# Abre el archivo en modo lectura ('r' indica lectura)
entrada = []
with open('trifelios.txt', 'r') as archivo:
    # Itera sobre cada línea del archivo
    for linea in archivo:
        # Procesa la línea
        removeSpace = linea.strip()  # Por ejemplo, aquí se imprime la línea sin caracteres de nueva línea
        splitStr = removeSpace.split("-")
        entrada.append(splitStr)

#Exp [['gato', 'toga'], ['codigo', 'digoco'], ['pato', 'topo'], ['el', 'le'], ['bronca', 'cabron']]



for i in range(len(entrada)):
    andresLectures = len(entrada[i][0])     #leer cuanto mide el string
    #Division String       
    #firstDivSplit =  entrada[i][0][:andresLectures//2]
    #scdDivSplit =   entrada[i][0][andresLectures//2:]
    #Comparision
    equal = entrada[i][1]
    #print(equal)
    #if firstDivSplit in equal and scdDivSplit in equal:
        #flag = True
    #else:
        #flag = False
    #flag = False
    for i in entrada[i][0]:
        if i not in equal:
            print("No es trifelio")
            break
    else:
        print("Es trifelio")

#Lo mas importante que aprendí aqui es a saber cuando termino un ciclo correctamente
#Agregando al final esa funcion else

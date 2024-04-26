#Dicts
twoDicts = {'opositivos':["sin embargo","no obstante","ahora bien","aun asi"],
            'causativos':["por tanto", "dado que", "por consiguiente", "asi pues", "por ende"]}

def removeStr(string): #algoritmo para elimar caracteres especificos que no quiero, no importan la cantidad
    palabrasEliminar = [',','.','\n']
    for i in range(len(palabrasEliminar)):
        for revisar in string:
            if revisar in palabrasEliminar[i]:
                dot = string.replace(palabrasEliminar[i],"")
                string = dot
    return string

organize = []
removeAnoyiing = []
with open(r'C:\Users\User\laptopProgramming\FundamentalsUNacional\Modulo 9\conversaciones.txt', 'r') as files: #cambiar dirección
    for file in files:
        strLower    =   file.lower()
        strsplit    =   strLower.replace(',','')
        quitarPuntos = strsplit
        hola = quitarPuntos.replace('.','')
        quitarnFeas = hola
        hola2 = quitarnFeas.replace('\n','')
        organize.append(hola2) #Como se maneja por filas hasta ahí podemos trabajar
        
#Algoritmo que revise de dos en dos las palabras para que encontremos los opositivos o causativos


for j in range(len(organize)):
    separador = organize[j].split(' ')
    opositivos = 0
    causativos = 0
    for i in range(len(separador)-1): 
        algoritmo = separador[i]+" "+separador[i+1]
        if algoritmo in twoDicts['opositivos']:
            opositivos += 1
        elif algoritmo in twoDicts['causativos']:
            causativos += 1
    print(f'Opositivos{opositivos} Causativos {causativos}')





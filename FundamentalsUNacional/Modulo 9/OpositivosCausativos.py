#Dicts
twoDicts = {'opositivos':["sin embargo","no obstante","ahora bien","aun asi"],
            'causativos':["por tanto", "dado que", "por consiguiente", "asi pues", "por ende"]}

def removeStr(string): #lo que aprendi es que hay que retornar lo que dio
    palabrasEliminar = [',','.','\n']
    for i in range(len(palabrasEliminar)):
        for revisar in string:
            if revisar in palabrasEliminar[i]:
                dot = string.replace(palabrasEliminar[i],"")
                string = dot
    return string

organize = []
removeAnoyiing = []
with open('conversaciones.txt', 'r') as files:
    for file in files:
        strLower    =   file.lower()
        strsplit    =   strLower.split(' ')
        organize.append(strsplit) #Como se maneja por filas hasta ahí podemos trabajar
        
for i in organize: #sirve para quitar simbolos que no sirven y para dejar trabajada la lista
    orgLista = []
    for j in i:
        sinMolestias = removeStr(j)
        orgLista.append(sinMolestias)
    removeAnoyiing.append(orgLista)
        
print(removeAnoyiing)


        
#Por cada fila tenemos que llenar ciertos parametros

#print("sin embargo" in twoDicts["causativos"]) #Identify seek


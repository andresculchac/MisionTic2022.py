lad,laele = {},[]
with open('matrix.txt', 'r') as fichero: 
    for linea in fichero: 
        try:
            linea.index('Smith:')
            linea.index('?')
            for i in linea[7:].replace('? ?','?').replace('?','-?-').split('?'):
                if i not in lad and i not in ['','\n','-'] and i[0] == '-' and i[-1] == '-' and i[1] != ' ' and i[-2] != ' ':
                    lad[i] = True
                    laele.append(i.replace('-','?'))
        except: pass
for i in laele: print(i)
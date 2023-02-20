N = int(input())
M = int(input())
MG = []
MGF = []
MGFN = []
for i in range(M):
  MG += [int(input())] #leemos los juegos y los guardamos en una lista
for j in range(N): #realizamos un recorrido por el numero de jugadores 
  if MG.count(j) > 1: #miramos si alguien gano mas de una vez
    MGF += [MG.count(j)] #guardamos el numero de veces que gano en una lista
    MGFN += [j] #guardamos el jugador que gano tratando de realizar un arreglo
X = max(MGF) # guardo en una variable el numero maximo de los ganadores
for k in range(len(MGFN)): #recorremos las listas buscando el o los que halan ganado mas 
  if MGF[k] == X:
    print(MGFN[k])
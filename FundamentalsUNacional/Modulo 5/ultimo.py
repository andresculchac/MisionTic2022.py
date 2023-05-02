entrada=int(input())
listaEntrante=[]
acumulador=0
acumulador2=0
for i in range(1,entrada+1):
    acumulador2=float(input()) #No era necesario multiplicar por algo, solo pedirlo en cada ciclo
    Jobb=i*acumulador2-acumulador
    Jobb=int(Jobb)
    acumulador+=Jobb
    listaEntrante.append(Jobb)
for ul in listaEntrante:
    print(ul)
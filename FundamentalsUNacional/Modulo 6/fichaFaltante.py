faltante=[]
restante=int(input())
fichas=restante
while restante>1:
   e=int(input())
   faltante.append(e)
   restante-=1

for j in range (1,fichas+1):
  if j not in faltante:
    print("La ficha faltante es la",j)
    break
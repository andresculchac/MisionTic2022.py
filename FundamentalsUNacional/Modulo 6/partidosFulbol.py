ballenotas = []
mandril = []
n = int(input()) #elemento que identifica cuantos numeros se van a poner 
for i in range(1,(n*2)+1):
    if i < n+1:
        h  = int(input())
        ballenotas.append(h)
    else:
        b = int(input())
        mandril.append(b)

# print(ballenotas)
# print(mandril)

# print(ballenotas)
# print(mandril)
#gana dos puntos
#empate 
# n = 5
# ballenotas = [2, 0, 0, 4, 0]
# mandril =    [3, 1, 1, 0, 2]


puntosballenotas = []
puntosmandril = []

for i in range(n):
    if ballenotas[i] == mandril[i]:
        n = 1
        puntosballenotas.append(n)
        puntosmandril.append(n)
    elif ballenotas[i] > mandril[i]:
        n = 2
        puntosballenotas.append(n)
    elif ballenotas[i] < mandril[i]:
        n = 2
        puntosmandril.append(n)
    

print("Ballenota Futbol Club:",sum(puntosballenotas))
print("Real Mandril:",sum(puntosmandril))
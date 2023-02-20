# variableX = True
# listaX = []
# while variableX:
#     variableJ = int(input())
#     if variableJ == 0:
#         variableX = False
#     listaX.append(variableJ) #inputs hasta poner el 0 se para 

# #despues hacer un for para que sume uno con uno xd

# for i in listaX:
#     print(i)
'''Eso era mio xd'''


ganadores=[ ]
keyx=0
while True:
  vine=int(input())
  if vine==0:
    break
  else:
    ganadores.append(vine)
for j in ganadores:
  complemento=1995-j
  if complemento in ganadores:
    keyx+=1
print(keyx//2)
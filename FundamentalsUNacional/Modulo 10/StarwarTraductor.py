#primero el funcionamientos de los diccionarios y luego los inputs y sus ciclos correspondientes 
def inputs(): #hacer una funcion que si pongo un n inputs pues se ejecute n veces #tipos de inputs
    request = int(input())
    while request>0:
      j = input()#Se evalua el tipo de entrada que se le va a poner ej: int, float, str ademas se pone el manejo de strings
      v = j.split(" ")
      a[v[0]] = v[1]
      request -= 1
    #print(a) #Guia para ver como van las salidas
a = {}  #aqui en ves de que todos se vayan para una lista debemos convertirlos en dict
#quiero hacer un split y en esa separacion el primer valor se va para key y el segundo se va para value
inputs()
def cycleinputs():
    request = int(input())
    while request>0:
      j = input() #Se evalua el tipo de entrada que se le va a poner ej: int, float, str ademas se pone el manejo de strings
      l.append(j)
      request -= 1
    #print(l) #Guia para ver como van las salidas

l = []
cycleinputs()
for i in range(len(l)):
  print(a.get(l[i],"palabra no encontrada"))

'''# diccionario = {"aargutcha":"sol", "akeeata":"viento",
# "bah-bah":"agua","balaloo":"arbol","traptaa":"comida"}

# h = ["bah-bah","aargutcha","bakte"]

# #print(h[1] in diccionario)

# for i in range(len(h)):
#   print(diccionario.get(h[i], "palabra no encontrada"))
# # print(diccionario.get(x[0],"palabra no encontrada"))
# # print(diccionario.get(p,"palabra no encontrada"))
# # print(diccionario.get(b,"palabra no encontrada"))
'''



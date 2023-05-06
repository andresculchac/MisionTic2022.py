#here i finished the point but the way that i complete the excersice was unexpected


x = True  #The point require find in a list the only numbers and if they repeat delete it.
lista = []
while x:
     y = int(input())
     request = lista.append(y)
     if y == 0:
        x = False
lista.pop(-1) #If the number is zero the inputs finish
#print(lista)


#lista = [21,47,35,658,47,1,100,9,35,47,] #algoritmo que me regresa solo los numeros que no estan repetidos
listaxD = []

for i in lista:
    if i not in listaxD:
        listaxD.append(i)

print(len(listaxD))
#que verguenza mano, como tres dias haciendo este problema para que sea asi de sencillo, lloroooooooooooo, pero lo acabe sin querer queriendo
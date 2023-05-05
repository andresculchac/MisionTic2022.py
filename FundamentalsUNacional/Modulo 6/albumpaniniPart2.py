x = True  #The point require find in a list the only numbers and if they repeat delete it.
lista = []
while x:
    y = int(input())
    request = lista.append(y)
    if y == 0:
        x = False
lista.pop(-1)
print(lista)
        


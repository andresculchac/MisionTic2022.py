required = 5
notrequired = required
inicio = 0


for i in range(required):
    for j in range(required):
        if inicio == j or j == notrequired-1:
             print("#",end="")
        else:
            print("0",end="")
    inicio += 1
    notrequired -= 1
    print(sep="/n")


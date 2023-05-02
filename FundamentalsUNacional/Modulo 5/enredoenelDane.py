pedirEntrada = int(input())
ListEmpty = []
remainder = 0 #stack of numbers day

for i in range(1,pedirEntrada+1):
    requestInput = float(input())
    myself = requestInput*i-remainder
    remainder += myself
    transformation = int(myself)
    addList = ListEmpty.append(transformation)

for i in ListEmpty:
    print(i)


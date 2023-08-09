weight = int(input())
height = int(input())


for i in range(height):
    for j in range(weight):
        if height //2 == i:
            print("+",end="")
        elif weight//2== j:
            print("+",end="")
        else:
            print("0",end="")
    print(sep="/n")
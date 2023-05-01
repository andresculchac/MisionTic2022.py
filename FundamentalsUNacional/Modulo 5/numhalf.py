#Identify HalfNumber

requestNum = int(input())

for i in range(requestNum):
    x = requestNum//2 
    if x == i:
        print("X")
    else:
        print(i)
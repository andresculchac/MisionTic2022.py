entrada = input()
entrada2 = input()
x = []
u = []

#Separacion de string mediante la fun(split())
string = entrada.split("x")
separate = entrada2.split("x")

#Entradas str a int
conv1 = [int(x) for x in string]
conv2 = [int(j) for j in separate]

print(conv1)
print(conv2)

k = max(conv1[0],conv1[1])
print(k)
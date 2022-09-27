num1 = int(input())
num1Estatico = num1
num2 = int(input())
num3 = int(input())
acumulador = 0 

for i in range(num2, num3+1):
    if num1 % i == 0:
        factor = num1 /i
        num1 = factor
        acumulador += 1
    else:
        print(num1Estatico,"no es polifactor entre",num2,"y",num3)

if acumulador == (num3+1)-num2:
    print(num1Estatico,"es polifactor entre",num2,"y",num3)
# print(i, acumulador)
# print("operacion:" ,(num3+1)-num2)
#print(num1Estatico,"es polifactor entre",num2,"y",num3) 

# else:
#     print(num1Estatico,"no es polifactor entre",num2,"y",num3)
    
num1 = int(input())
num1Estatico = num1
num2 = int(input())
num3 = int(input())

for i in range(num2, num3+1):
    factor =num1/i
    num1 = factor
    # if factor%i ==0:
    #     print(factor)
if num1 == 1:
    print(num1Estatico,"es polifactor entre",num2,"y",num3)    
else:
    print(num1Estatico,"no es polifactor entre",num2,"y",num3)
    
num1 = float(input())
num2 = float(input())
num3 = float(input())

if num1 < num2 and num3 > num1 and num2 > num3:
    print((num1 + num2 + num3)/3)
#3.0 4.0 5.0 ejemplo para que de la mediana
elif num1 <num2 and num2 < num3 and num3 > num1:
    print(num2,"es la mediana")
# 5.0 3.0 1.0 ejemplo para esta 
elif num1 > num2 and num2 > num3 and num3 < num1:
    print(num1, "es la mediana")
# 444.44 555.55 333.33
elif num1 < num2 and num2 > num3 and num3 < num1:
    print(num1,"es la mediana")
if num1 > num2 and num2 < num3 and num3 == num1:
    print(num1,"es la mediana")
if num1 == num2 and num2 == num3  and num3 == num1:
    print(num1,"es la mediana")
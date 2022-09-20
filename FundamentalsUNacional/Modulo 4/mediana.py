num1 = float(input())
num2 = float(input())
num3 = float(input())

#3.0 5.0 4.0
if num1 <num2 and num2 > num3 and num3> num1:
    print(num3,"es la mediana")
#3 1 2
elif num1 > num2 and num2 < num3 and num3<num1:
    print(num3,"es la mediana")
#3.0 4.0 5.0 ejemplo para que de la mediana
elif num1 <num2 and num2 < num3 and num3 > num1:
    print(num2,"es la mediana")
# 5.0 3.0 1.0 ejemplo para esta 
elif num1 > num2 and num2 > num3 and num3 < num1:
    print(num1, "es la mediana")
#10 20 20
elif num1 < num2 and num2 == num3 and num3 > num1:
    print(num2 ,"es la mediana")
#20 20 10
elif num1 ==  num2 and num2 > num3 and num3 < num1:
    print(num2,"es la mediana")
# 70 10 80
elif num1 > num2 and num2 < num3 and num3 > num1:
    print(num1,"es la mediana")
# 444.44 555.55 333.33
elif num1 < num2 and num2 > num3 and num3 < num1:
    print(num1,"es la mediana")
if num1 > num2 and num2 < num3 and num3 == num1:
    print(num1,"es la mediana")
if num1 == num2 and num2 == num3  and num3 == num1:
    print(num1,"es la mediana")

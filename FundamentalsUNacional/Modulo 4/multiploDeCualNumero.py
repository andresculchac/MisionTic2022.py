num1 = int(input())

if num1 %2 == 0:
    print(num1,"es multiplo de 2")
    print('N es multiplo de 2')
elif num1 %3 == 0:
    print(num1,"es multiplo de 3")
elif num1 %5 == 0:
    print(num1,"es multiplo de 5")
elif num1 %7 == 0:
    print(num1,"es multiplo de 7")
else:
    print(num1,"no es multiplo de ninguno de los primeros cuatro primos")
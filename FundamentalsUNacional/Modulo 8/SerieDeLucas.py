
#Como crear una funcion xD

def fib(n):
    if n == 0:
        return 0
    elif n==1:
        return 2
    elif n==2:
        return 1
    return (fib(n-1)+fib(n-2))

a = 200 
b = 300
contador = 0    
for i in range(10000000):
    if fib(i) >= a and fib(i)<= b:
        contador += 1
    if fib(i)>b:
        break
print(contador)


    

    





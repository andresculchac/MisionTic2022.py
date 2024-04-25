# vamos a hacer una demostracion y un pequeño avance en cuestiones de 
# el el reto tres de mision tic 

values = [1,2,2,3,3,3,1,2,3,5,6,5,6,7,13]
repeat = []
unique = []
resultSum = 0

for i in values :
    if i not in unique:
        unique.append(i)
    else:
        resultSum += i
        if i not in repeat:
            repeat.append(i)

print("Los valores sin repetición son:", unique)
print("Los valores que se repiten son:", repeat)
print("La suma de los valores repetidos es:", resultSum)
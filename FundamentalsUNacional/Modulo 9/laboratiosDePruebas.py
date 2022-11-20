contador = 0
almacen = []
listaPorSiAcaso = []

a = ["obelix","julianicus","pedro","Dhalekanya","nicolax"]
for i in range(len(a)):
    if a[i][-1:] == "a": #algoritmo para identificar a los indios
        amabilidad = a[i][-1:]
        almacen.append(amabilidad)
        if amabilidad == "a":
            print("Indios")
    
    robar =a[i][-2:]
    almacen.append(robar)
    if robar == "ix":
        print("Galo")
    if robar == "us":
        print("Romano")
    if robar == "ic":
        print("Godos")
    if robar == "as":
        print("Griegos")
    if robar == "af":
        print("Normandos")    
    if robar == "is" or robar == "ax":
        print("Bretones")
    if robar == "ez":
        print("Hispanos")
    
            
            
            

print(almacen)
print()
print()
#necesito capturar a los dos primeros y compararlos y asi sucesivamente
#objetivo sacarlos desde el principio ordenados ya para no romperme la cabeza por aca


    
    


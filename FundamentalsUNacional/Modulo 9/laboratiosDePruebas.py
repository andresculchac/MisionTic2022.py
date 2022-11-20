contador = 0
almacen = []
listaPorSiAcaso = []
a = ["obelix","extreme","ave"]
for i in range(len(a)):
    contador = 0
    for b in a[i]:
        z = len(a[i])
        contador +=1
        if contador == z-1:
            almacen.append(b)
            
        if contador == z:
            almacen.append(b)
            


print(almacen)
print()
print()
#necesito capturar a los dos primeros y compararlos y asi sucesivamente
#objetivo sacarlos desde el principio ordenados ya para no romperme la cabeza por aca


    
    


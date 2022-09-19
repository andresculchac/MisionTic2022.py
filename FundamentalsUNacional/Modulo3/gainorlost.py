capitalInical = int(input()) #son enteros porque los ejemplos solo manejan enteros
retornoK = int(input())
equation = ((retornoK-capitalInical)/capitalInical)*100

if retornoK>capitalInical:
    
    print("Hubo una ganancia de $",retornoK-capitalInical,"correspondiente al",equation,"% del capital invertido")
elif retornoK<capitalInical:
    
    print("Hubo una perdida de $",capitalInical-retornoK,"correspondiente al",equation*-1,"% del capital invertido")
else:
    print("No hubo ni ganancia ni perdida, la inversion fue un desperdicio de tiempo, pero al menos no de dinero")
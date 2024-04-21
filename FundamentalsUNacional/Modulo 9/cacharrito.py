
impresionFinal = []
#example = "ABC123 DEF456 GHI789"
NumeroDeSolicitudes = int(input())
for i in range(NumeroDeSolicitudes):
    placa = input()
    jorge = placa.split(" ")
    MiPlaca = 0

    for i in jorge[0]:
        MiPlaca += ord(i)




    for i in jorge:
        contador = 0
        for j in i:
            contador += ord(j)
        if MiPlaca > contador: 
            impresionFinal.append(f"Al menos otro auto es mas viejo que mi cacharrito :(")   
            break
            
    if MiPlaca < contador: #Si de mi placa inicial se mantiene igual imprime
        impresionFinal.append(f"Mi cacharrito es el mas viejo de todos los autos ;D")
        

for x in impresionFinal:
    print(x)
        

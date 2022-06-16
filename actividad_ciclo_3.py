
# lista_entrada = A,A,a,c,g,c,B,A,F,f,b,f,E,b,f,b







entrada = input().upper().split(",")

lista_letras = []
lista_contadores_letras_consecutivas = []
muestra = entrada[0]
conteo =  1
entrada.append("0")
for i in range(1, len(entrada)):
    if entrada[i] == muestra:
        print(entrada[i])
        conteo = conteo + 1
        muestra = entrada[i].upper()
        
        
    else:
        lista_letras.append(muestra)
        lista_contadores_letras_consecutivas.append(str(conteo))
        muestra = entrada[i]
        conteo = 1
    

print(",".join(lista_letras),",".join(lista_contadores_letras_consecutivas),sep="\n")
    

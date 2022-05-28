# es esta cadena vamos a recibir una lista y la vamos a sacar si comas y en mayusculas como primer paso 



lista_chichipata = "jkdsjfkjaskdfj;asldjf;sadkjfksd"
lista = "A,A,a,c,g,c,B,A,F,f,b,f,E,b,f,b".upper()
lista_sin_commas = lista.replace(",", "")
print(lista_sin_commas)

for recorrido in lista_sin_commas:
    if recorrido in lista_sin_commas:
        

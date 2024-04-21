

#example = "ABC123 DEF456 GHI789"

placa = "ZZZ999"


contador = 0
for i in placa:
    for j in i:
        contador += ord(j)
        

print(contador)

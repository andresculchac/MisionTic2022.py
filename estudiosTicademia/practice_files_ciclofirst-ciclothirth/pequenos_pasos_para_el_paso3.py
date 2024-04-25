# i = a
# a
# b
# a
# a

xd = ["a", "a", "b", "a", "a"]                      #objetivos que me diga que hay dos a una b  y dos a mi dream wet
otra_manera_de_guardar_el_numero = []
muestra = xd[0]
guardamoselnumero = []
contador = 1
for i in range(1, len(xd)):
    if xd[i] == muestra:
        contador += 1
        otra_manera_de_guardar_el_numero.append(contador)
        muestra = xd[i]

print(contador)
print(guardamoselnumero)
print(otra_manera_de_guardar_el_numero)

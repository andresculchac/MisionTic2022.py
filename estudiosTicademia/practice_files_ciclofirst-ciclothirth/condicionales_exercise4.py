# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

age = int(input("how old are you"))
taxes = int(input("what is your salary yearly"))
if age >15:
    if taxes >=1000:
        print("you're have that pay taxes ")



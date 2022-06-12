# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
#  El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto
# . Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
sex_students = input("what is your gender?") 
name_students = input("What's your name?")
name = (name_students[0]) #con esta variable toma la primera letra de el nombre

# asigno las letras a las variables para despues ver si coinciden name con la letra que piden ps
grupo_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
grupo_a_male = ["n", "ñ", "o", "p", "q", "r", "s", "t", "u",  "v", "w", "x", "y", "z"]


# condicionales para mujeres 
if sex_students == "female":
    if name in grupo_a:   #el in sirve para preguntar si la variable name esta dentro de la variable grupo a 
        print("pertenece al grupo a ")
    elif name != grupo_a:
            print("perteneces al grupo b")

# condicionales para hombres 
if sex_students == "male":
    if name in grupo_a_male:
        print("pertenece al grupo a ")
    elif name != grupo_a_male:
        print("perteneces al grupo b")


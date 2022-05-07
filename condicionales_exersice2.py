


user = "andres"
password = "andresito123"
userquestion = input("What is your user?")
passwordquestion = input("What is your password?")

if userquestion == user:
    if passwordquestion == password:
        print("Welcome to the website")
else:
    print("Access denied")
#el proximo reto es hacer como el docente que lo que hacia era poner esto en un bucle 
# de tal manera que hasta que no estuviera bien se volvia a repetir

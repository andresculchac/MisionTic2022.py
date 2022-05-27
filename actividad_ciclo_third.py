
# ideas, primero hay que hacer como un contador que realice la suma de las letras 
# por medio del codigo asccii quizas podamos hacer un contador que haga ese procedimiento
# y pues si me complico mucho la vida vemos las guias del docente, pero primero hacerlo solo
# tiempo de preparacion 2 horas 

entradafirst =  input().upper().replace(",", "")

for letras in entradafirst:
    print(letras, ord(letras))


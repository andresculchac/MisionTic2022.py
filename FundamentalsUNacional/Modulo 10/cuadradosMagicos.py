Exm = [[16, 3, 2, 13],
       [5, 10, 11, 8],
       [9, 6, 7, 12],
       [4, 15, 14, 1]]

RequestNum = 1
"""
Caso 1 
16 3 2 13 
5 10 11 8 
9 6 7 12 
4 15 14 1
"""
matrix = []
for i in range(RequestNum):#entrada de la matrix
    for j in range(5):
        requestInput = input()
        matrix.append(requestInput)
#modificación de la matrix
editList = matrix.pop(0) #Remueve el caso uno que no sirve para nada

matrixInt = []
for i in matrix:
    listMatrixInterna = []
    splitStr = i.split(' ')
    for j in splitStr:
        if j == '':
            continue
        else:
            listMatrixInterna.append(int(j))
    matrixInt.append(listMatrixInterna)
print(matrixInt)

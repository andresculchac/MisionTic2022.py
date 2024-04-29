
printOuput = []
RequestNum = int(input())

for i in range(RequestNum):#entrada de la matrix
    matrix = []
    for j in range(5):
        requestInput = input()
        if j == 0:
            continue
        else:
            splitStr = requestInput.split(' ',3)
            matrixInterna = []
            for stringsitos in splitStr:   
                matrixInterna.append(int(stringsitos))
            matrix.append(matrixInterna)

    isMagic = sum(matrix[0])
    filas = True
    columnas = True
    diagonales = True

    for i in range(4): #filas
        if sum(matrix[i]) != isMagic:
            filas = False
            break

    #columnas

    for i in range(4):
        isColumna = 0
        for j in range(4):
            x = matrix[j][i]
            isColumna += x
        if isColumna != isMagic:
            columnas = False
            break

    #diagonales
    allslash = 0
    for i in range(4):
        x = matrix[i][i]
        inverseSlash = matrix[i][3-i]
        allslash += inverseSlash
        allslash += x

    if allslash/2 != isMagic:
        diagonales = False

    if filas and columnas and diagonales:
        printOuput.append("cuadrado magico")
    else:
        printOuput.append("cuadrado muggle")

for _ in printOuput:
    print(_)

# matrixAll = [[16,  3,  2, 13],
#             [ 5,  10, 11,  8],
#             [ 9,   6,  7, 12],
#             [ 4,  15, 14,  1]]
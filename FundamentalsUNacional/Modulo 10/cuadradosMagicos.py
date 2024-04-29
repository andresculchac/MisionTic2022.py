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
        if j == 0:
            continue
        else:
            splitStr = requestInput.split(' ',3)
            matrixInterna = []
            for stringsitos in splitStr:   
                matrixInterna.append(int(stringsitos))
            matrix.append(matrixInterna)

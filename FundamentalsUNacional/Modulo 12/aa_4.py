def inicio_final(zucchini,n) -> bool:
    for diag in range(len(zucchini)):
        zila = range(diag) if n == 1 else range(diag+1,len(zucchini))
        for j in zila:
            if zucchini[diag][j] != 0: return True
    return False


for i in range(int(input())):
    zucchini = []
    for kil in range(int(input())): zucchini.append(list(map(float,input().split())))
    sup, inf = inicio_final(zucchini,0) , inicio_final(zucchini,1)
    triangulos = 'Ni diagonal ni triangular' if sup == True and inf == True else 'Triangular superior' if sup == True and inf == False else 'Triangular inferior' if sup == False and inf == True else 'Diagonal'
    #i = (1+zucchini)
    print(triangulos)
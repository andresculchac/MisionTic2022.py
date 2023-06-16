def ma_tri(zun,n) -> bool:
    for diag in range(len(zun)):
        zila = range(diag) if n == 1 else range(diag+1,len(zun))
        for j in zila:
            if zun[diag][j] != 0: return True
    return False


for i in range(int(input())):
    zun = []
    for kil in range(int(input())): zun.append(list(map(float,input().split())))
    sup, inf = ma_tri(zun,0) , ma_tri(zun,1)
    triangulos = 'Ni diagonal ni triangular' if sup == True and inf == True else 'Triangular superior' if sup == True and inf == False else 'Triangular inferior' if sup == False and inf == True else 'Diagonal'
    #i = (1+zun)
    print(triangulos)
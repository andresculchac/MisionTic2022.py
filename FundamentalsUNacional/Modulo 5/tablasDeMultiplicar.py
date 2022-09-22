N = int(input())

contador = 0
if N <= 20:
    for i in range (1,21):
        multiplicador = N*i
        print(N, "x",i,"=",multiplicador)
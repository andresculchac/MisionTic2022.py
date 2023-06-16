for anagrama in range(int(input())):
    xy, suprimir_anagrama = input().replace(" ","").split(':'), "Es anagrama"
    for i in xy[1]:
        if i in xy[0]: xy[0] = xy[0].replace(i,'',1)
        else: suprimir_anagrama = 'No es anagrama';break
    if len(xy[0]) != 0 : suprimir_anagrama = 'No es anagrama'
    print(suprimir_anagrama)
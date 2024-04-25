from datetime import datetime


for stadistic in range(int(input())):
    keylistX,impresion = input().split(), 0


    for listz in range(int(keylistX[1])):
        if datetime.strptime(f"{int(keylistX[0][:4])+listz+1}{keylistX[0][4:]}","%Y/%m/%d").weekday() == 0: impresion += 1
    print(impresion)
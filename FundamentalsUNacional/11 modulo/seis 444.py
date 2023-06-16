from datetime import datetime
for estadistica in range(int(input())):
    keylistX,result = input().split(), 0
    for listz in range(int(keylistX[1])):
        if datetime.strptime(f"{int(keylistX[0][:4])+listz+1}{keylistX[0][4:]}","%Y/%m/%d").weekday() == 0: result += 1
    print(result)
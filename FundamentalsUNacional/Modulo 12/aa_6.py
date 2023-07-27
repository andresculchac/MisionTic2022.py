from datetime import datetime
for _ in range(int(input())):
    seconds, last, dif, es = input().split(', '), 0, None, True
    for _ in range(int(seconds[1])):
        act = datetime.strptime(input(),'%Y-%m-%d')
        if last != 0 :
            diftemp = act - last
            if dif == None: dif, last = diftemp, act ; continue
            if diftemp != dif : es = False
            dif = diftemp
        last = act
    if es == False: print(f'{seconds[0]} no es asesino(a) serial periodico\n');continue
    print(f'{seconds[0]} ataca cada {dif.days} dias y volvera a hacerlo en {(last+dif).strftime("%Y-%m-%d")}\n')
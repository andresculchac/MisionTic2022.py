from datetime import datetime
decepcion, solaris, notar = None,0, int(input())
def no_lift(dif): 
    diari = int(dif/86400)
    dif %= 86400
    bila = int(dif/3600)
    dif %= 3600
    mom = int(dif/60)
    onds = int(dif%60)
    return f'{diari} dias, {bila} horas, {mom} minutos, {onds} segundos'
for bi in range(notar):
    s = datetime.strptime(input(), '%Y-%m-%d %X')
    if decepcion != None:  
        clock = s-decepcion
        solaris += clock.total_seconds() 
        print(no_lift(int(clock.total_seconds())))
    decepcion = s
print(f'\nPromedio: {no_lift(int(solaris/(notar-1)))}')
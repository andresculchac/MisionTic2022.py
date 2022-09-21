horas = int(input())
minutos = int(input())
espejoHoras = 11 - horas
espejoMinutos = 60 - minutos

if minutos == 0 and minutos < 10 and horas != 12:
    conversion = 12-horas
    #print(conversion,(":"),minutos)
    print(str(conversion)+":"+str(minutos))
    #print("test 0")
if minutos == 0 and minutos < 10 and horas == 12:
    if horas == horas:
        print(str(horas)+":"+str(minutos))
    elif horas != horas:
        conversion = 13-horas
    #print(conversion,(":"),minutos)
        print(str(conversion)+":"+str(minutos))



elif minutos == 0 and minutos >= 10:
    conversion = 12-horas
    #print(conversion,":", espejoMinutos)
    print(str(conversion)+":"+str(espejoMinutos))
    #print("test 1")
#elif minutos == 0 and minutos >= 10:





if minutos != 0 and espejoHoras != 0 and espejoHoras != -1:
    conversion = 11 - horas
    #print(conversion,(":"), espejoMinutos)
    print(str(conversion)+":"+str(espejoMinutos))
    #print("test cabron")

elif espejoHoras == 0:
    correccion = espejoHoras =12
    print(str(correccion)+":"+str(espejoMinutos))
    #print("test holi")

elif espejoHoras == -1 and minutos!=0:
    correccion = espejoHoras = 11
    print(str(correccion)+":"+str(espejoMinutos))
    #print("test chao")




horas = int(input())
minutos = int(input())
espejoHoras = 11 - horas
espejoMinutos = 60 - minutos

if minutos == 0 and minutos < 10:
    conversion = 12-horas
    #print(conversion,(":"),minutos)
    print(str(conversion)+":"+str(minutos))

elif minutos == 0:
    conversion = 12-horas
    #print(conversion,":", espejoMinutos)
    print(str(conversion)+":"+str(espejoMinutos))




if minutos != 0 and espejoHoras != 0:
    conversion = 11 - horas
    #print(conversion,(":"), espejoMinutos)
    print(str(conversion)+":"+str(espejoMinutos)+"test 2")


elif espejoHoras == 0:
    correccion = espejoHoras =12
    #print(correccion,(":"),espejoMinutos)
    print(str(correccion)+":"+str(espejoMinutos)+"test 3")
    



dineroBanco = int(input())
dineroQueVaQuedando = 0

'''problemas con '''
if dineroBanco >= 0 and dineroBanco <= 1000000:
    x = dineroBanco //50000
    conversion = x*50000
    restante = dineroBanco - conversion
    dineroQueVaQuedando += restante
    if x != 0:
        print(x,"de $50000")

    if dineroQueVaQuedando //20  != 0 and dineroQueVaQuedando >=20000:
        x = dineroQueVaQuedando //20000
        conversion = dineroQueVaQuedando*50000
        conversion = dineroQueVaQuedando-x*20000
        dineroQueVaQuedando = conversion
        if x != 0:
            print(x,"de $20000")

    if dineroQueVaQuedando //10  != 0:               #con 10 mil 
        x = dineroQueVaQuedando //10000
        conversion = dineroQueVaQuedando-x*10000
        dineroQueVaQuedando = conversion
        if x != 0:
            print(x,"de $10000")

    if dineroQueVaQuedando //5  != 0:               #con 5 mil 
        x = dineroQueVaQuedando //5000
        conversion = dineroQueVaQuedando-x*5000
        dineroQueVaQuedando = conversion
        if x != 0:
            print(x,"de $5000")

    if dineroQueVaQuedando //2  != 0:               #con 2 mil 
        x = dineroQueVaQuedando //2000
        conversion = dineroQueVaQuedando-x*2000
        dineroQueVaQuedando = conversion
        if x != 0:
            print(x,"de $2000")

    if dineroQueVaQuedando //1  != 0:               #con  mil 
        x = dineroQueVaQuedando //1000
        conversion = dineroQueVaQuedando-x*1000
        dineroQueVaQuedando = conversion
        if x != 0:
            print(x,"de $1000")
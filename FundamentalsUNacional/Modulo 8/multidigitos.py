#multidigitos made by Andres Culchac

def isMultidigito(num):
    multidigit = [1,2,3,4,5]
    digitos = []
    while num>0:
        #primero sacamos el ultimo digito
        digito = num%10
        digitos.insert(0,digito)
        num = num//10
    for i in multidigit:
        if i not in digitos:
            return False
    return True

flag = True
impresionFinal = list()
while flag:
    solicitar = int(input())
    if solicitar != 0:
        if isMultidigito(solicitar):
            impresionFinal.append(f'Multidigito')
        else:
            impresionFinal.append(f'No es multidigito')
    else:
        flag = False

for i in impresionFinal:
    print(i)


yy = [5,6,7,8,9]

def orden(lista):
    for i in range(len(lista)):
        if lista[0] + i == lista[i]:
            if lista[0]+1 != lista[1]:
                return False          
        else:
            return False
            break
    return True
        
        
print(orden(yy))


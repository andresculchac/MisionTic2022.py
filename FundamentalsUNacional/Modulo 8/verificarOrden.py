yy = [5,6,7,20,9]

def orden(lista):
    for i in range(len(lista)):
        if lista[0] + i == lista[i]:
            if lista[0]+1 == lista[1]:
                continue
            else:
                return False
                break
            
        else:
            return False
            break
    return True
        
        
print(orden(yy))


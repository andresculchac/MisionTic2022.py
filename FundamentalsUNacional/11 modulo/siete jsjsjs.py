from collections import deque
from random import randint

j = []
for inicio in range(int(input())):
    randit_1, sinergy_init, avz1, prote_b, red = list(range(1,14))*4 , 0 , 0, deque(), deque(map(int, input().split()[1:]))
    try: 
        for i in red: randit_1.remove(i)
    except: ""
    #avance for final
    for j in range(10):
        init = []
        avz2 = []
        a = randint(0,len(randit_1)-1)
        prote_b.append(randit_1.pop(a))
    for intermedio in range(10):
        ch, cp = prote_b.pop(), red.pop()
        sinergy_init,avz1 = sinergy_init+1 if ch>cp else sinergy_init , avz1+1 if cp>ch else avz1
    print(f"Puntos humano:{sinergy_init} Puntos plataforma: {avz1}")
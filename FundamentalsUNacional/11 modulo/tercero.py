import random
def data(init_inputrange):
    sinfin = random.randint(1,6) + random.randint(1,6)
    nitre = "Gana el sinfinumano" if sinfin>init_inputrange else "Gana la plataforma" if sinfin<init_inputrange else "Empate"
    print(nitre)

    
for quality in range(int(input())): data(int(input().split()[1]))
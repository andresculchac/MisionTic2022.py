listxxx=int(input())
keybord=[]
Acumula=0
siner=0
for i in range(1,listxxx+1):
    siner=float(input())
    Jobb=i*siner-Acumula
    Jobb=int(Jobb)
    Acumula+=Jobb
    keybord.append(Jobb)
for ul in keybord:
    print(ul)
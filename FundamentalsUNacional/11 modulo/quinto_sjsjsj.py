#dificil pero entretendio laverdad
from datetime import datetime
cillac, hva= datetime.strptime("00:00:00",'%X') - datetime.strptime("00:00:00",'%X'), 0
for inicio in range(int(input())):
    listxx = input().split(", ")
    if listxx[1] == "barberia":
        iuuu , hva = datetime.strptime(listxx[3],'%X') - datetime.strptime(listxx[2],'%X'), hva+1
        cillac += iuuu
print(f"{hva} veces\n{int((cillac.total_seconds()/(hva))//3600)} horas, {int(((cillac.total_seconds()/(hva))%3600)//60)} minutos, {int(((cillac.total_seconds()/(hva))%3600)%60)} segundos")
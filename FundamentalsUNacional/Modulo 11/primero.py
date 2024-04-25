import datetime
def     quarentine(s1,s2):
    spmkt = datetime.datetime.strptime(s1, "%Y-%m-%d")
    cmpter = datetime.datetime.strptime(s2, "%Y-%m-%d")
    kebard = cmpter-spmkt
    print(f"{kebard.days} dias = {int(kebard.total_seconds()//3600)} horas = {int(kebard.total_seconds()//60)} minutos = {int(kebard.total_seconds())} segundos")
for molsta in range(int(input())):
    pcil = input().split()
    quarentine(pcil[1],pcil[2])
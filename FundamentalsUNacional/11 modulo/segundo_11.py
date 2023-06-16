from datetime import datetime
kbard = {"true vampires": 0, "early birds":0 ,"sunny warmers":0 ,"lunch workers":0 ,"sunset lovers":0 ,"prime timers":0}
mnior = ['true vampires','early birds','sunny warmers','lunch workers','sunset lovers', "prime timers"]
sin = datetime.strptime("00:00:00", "%X").time()
ergia = datetime.strptime("04:00:00", "%X").time()
bolac = datetime.strptime("08:00:00", "%X").time()
bolac122 = datetime.strptime("12:00:00", "%X").time()
ergia121 = datetime.strptime("16:00:00", "%X").time()
gila = datetime.strptime("20:00:00", "%X").time()
kilobo = datetime.strptime("23:59:59", "%X").time()
def horas_io(h):
    act = datetime.strptime(h, "%X").time()
    if sin <= act < ergia: kbard["true vampires"] += 1
    if ergia <= act < bolac: kbard["early birds"] += 1
    if bolac <= act < bolac122: kbard["sunny warmers"] += 1
    if bolac122 <= act < ergia121: kbard["lunch workers"] += 1
    if ergia121 <= act < gila: kbard["sunset lovers"] += 1
    if gila <= act <= kilobo: kbard["prime timers"] += 1

for nnnnnnnn in range(int(input())): horas_io(input().split()[1])
for i in range(6): print(f"{mnior[i]} {kbard[mnior[i]]}")
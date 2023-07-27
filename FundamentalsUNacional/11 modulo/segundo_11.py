from datetime import datetime
scheduleTimer = {"true vampires": 0, "early birds":0 ,"sunny warmers":0 ,"lunch workers":0 ,"sunset lovers":0 ,"prime timers":0}
programming = ['true vampires','early birds','sunny warmers','lunch workers','sunset lovers', "prime timers"]
timer1 = datetime.strptime("00:00:00", "%X").time()
ergia = datetime.strptime("04:00:00", "%X").time()
bolac = datetime.strptime("08:00:00", "%X").time()
bolac122 = datetime.strptime("12:00:00", "%X").time()
ergia121 = datetime.strptime("16:00:00", "%X").time()
gila = datetime.strptime("20:00:00", "%X").time()
kilobo = datetime.strptime("23:59:59", "%X").time()
def horas_io(h):
    act = datetime.strptime(h, "%X").time()
    if timer1 <= act < ergia: scheduleTimer["true vampires"] += 1
    if ergia <= act < bolac: scheduleTimer["early birds"] += 1
    if bolac <= act < bolac122: scheduleTimer["sunny warmers"] += 1
    if bolac122 <= act < ergia121: scheduleTimer["lunch workers"] += 1
    if ergia121 <= act < gila: scheduleTimer["sunset lovers"] += 1
    if gila <= act <= kilobo: scheduleTimer["prime timers"] += 1

for nnnnnnnn in range(int(input())): horas_io(input().split()[1])
for i in range(6): print(f"{programming[i]} {scheduleTimer[programming[i]]}")
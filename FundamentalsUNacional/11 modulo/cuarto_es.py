from datetime import datetime
def data(input):
    disno, keyboard = datetime.strptime(input,'%I:%M:%S %p') , datetime.strptime("00:00:00",'%X')
    print(F"Loading day ... {round((disno-keyboard).total_seconds()/864,3)}%")
for _ in range(int(input())): data(input())
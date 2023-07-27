from datetime import datetime
# j={{{
#   #sinergy_init, avz1, prote_b, red = list(range(1,14))*4 , 0 , 0, deque(), deque(map(int, input().split()[1:]))  
# }}}
month_init = {1:"Enero",2:"Febrero",3:"Marzo",4:'Abril',5:'Mayo',6:'Junio',7:'Julio',8:'Agosto',9:'Septiembre',10:'Octubre',11:'Noviembre',12:'Diciembre'}
def google_calendar_self(yya, m):
    diferent , calendar_init_self = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31} , datetime.strptime(f'1/{m}/{yya}','%d/%m/%Y').weekday()
    diferent[2] = 29  if yya%4 == 0 and (yya%100 != 0 or yya%400==0)else 28
    print('lun\tmar\tmie\tjue\tvie\tsab\tdom')
    for minami in range(calendar_init_self): print("\t",end="")
    for i in range(1,diferent[m]+1):
        if i != 1 and calendar_init_self!= 0: print(f"\t{i}",end="")
        else: print(i,end="")
        calendar_init_self += 1
        if calendar_init_self == 7:
            k = []
            calendar_init_self=0
            if i!=diferent[m]: print()
randint_datetime1 = int(input())
if randint_datetime1 == -1:
    a = int(input("Qué año?\n"))
    for i in range(1,13):
        i = {}
        b = {}
        print("___________________________________________________ "+month_init[i])
        google_calendar_self(a,i)
        print()
else:
    for jbl in range(randint_datetime1):
        calendar_init_self = list(map(int,input().split("/")))
        google_calendar_self(calendar_init_self[2],calendar_init_self[1])
        print("\n")

# #if randint_datetime1 == -1:
#     a = int(input("Qué año?\n"))
#     for i in range(1,13):
#         i = {}
#         b = {}
#         print("___________________________________________________ "+month_init[i])
#         google_calendar_self(a,i)
#         print()
# #
from datetime import datetime
for zeller in range(int(input())):
    history,nothing = input().split(), ""
    xy, hilux = datetime.strptime(history[0],"%d-%m-%Y"),datetime.strptime(history[1],"%d-%m-%Y")
    case = hilux-xy
    for inazuma in range(int(case.days//5)): nothing += "5 "
    for notation in range(int(case.days%5)): nothing += "1 "
    print(nothing[:-1])
x,y = int(input()),int(input())
resta = y-x

if resta % 4 == 0:
    print(resta)
elif resta % 10 == 0 or resta % 15 == 0:
    print(resta)
    print("y te lo puedes quedar")
requestStr = int(input())
reggaeton = {}
rock = {}


for i in range(requestStr):
    requestInterno = input()
    splitRequest = requestInterno.split(' ')
    for i in range(len(splitRequest)-1):
        if splitRequest[i] is not reggaeton:
            reggaeton[splitRequest[i]]= 0

requestStr2 = int(input())
for i in range(requestStr2):
    requestInterno2 = input()
    splitRequest2 = requestInterno2.split(' ')
    for i in range(len(splitRequest2)-1):
        if splitRequest2[i] is not rock:
            rock[splitRequest2[i]]= 0
    
print(f"Reggaeton: {len(reggaeton)} Rock: {len(rock)}")


#width,height = int(input()),int(input())
#The Prints going to one by one
#Discover the half
    #add conditional
#First Step : Discover the table with zero
# def mitaddebandera():
#     for i in range(height):
#         halfnum = height // 2
#         if halfnum == i:
#             print("+"*width)
#         else:
#             print("0"*width)


ancho = int(input()) 
altura = int(input())
                                                        

for i in range(altura): 
    fila = ""
    for x in range(ancho):
        if x == ancho//2 or i == altura//2:
            fila += "+"  
        else:
            fila += "0"       
    print(fila)
    
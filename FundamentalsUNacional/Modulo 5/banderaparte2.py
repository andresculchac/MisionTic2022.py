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

altura = 7
ancho = 5                                                               

for i in range(altura):
    for j in range(ancho): 
        if j == 0:
            ceros = "0"
        if j == 2:
            ultimos = "0"
        else:
            mases = "+"
    print(ceros,mases,ultimos)
    
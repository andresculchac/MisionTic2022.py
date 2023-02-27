simpleX = float(input())
simpleY = float(input())

#algorithm to axes
#no sabia que se podia agrupar en un parentesis dos cosas como estas y salen los parentesis
if (simpleX > 0.0 or simpleX< -0.0) and simpleY == 0.0 :
    print("La coordenada",(simpleX, simpleY),"esta sobre el eje X") 
elif simpleX == 0.0 and  (simpleY > 0.0 or simpleY < -0.0):
        print("La coordenada",(simpleX, simpleY),"esta sobre el eje Y")  
elif simpleX == 0.0  and simpleY == 0.0:
        print("La coordenada",(simpleX, simpleY),"corresponde al origen")
#for quadrants
if simpleX > 0.0 and simpleY > 0.0:
    print("La coordenada",(simpleX, simpleY),"se encuentra en el cuadrante 1")
    
elif simpleX < -0.0 and simpleY > 0.0:
    print("La coordenada",(simpleX, simpleY),"se encuentra en el cuadrante 2")
elif simpleX< -0.0 and simpleY < -0.0:
    print("La coordenada",(simpleX, simpleY),"se encuentra en el cuadrante 3")
    
elif simpleX> 0.0 and simpleY< -0.0:
    print("La coordenada",(simpleX, simpleY),"se encuentra en el cuadrante 4")

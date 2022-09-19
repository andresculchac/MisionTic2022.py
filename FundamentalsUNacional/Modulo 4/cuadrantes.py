xx = float(input())
yy = float(input())

#algorithm to axes
#no sabia que se podia agrupar en un parentesis dos cosas como estas y salen los parentesis
if (xx > 0.0 or xx< -0.0) and yy == 0.0 :
    print("La coordenada",(xx, yy),"esta sobre el eje X") 
elif xx == 0.0 and  (yy > 0.0 or yy < -0.0):
        print("La coordenada",(xx, yy),"esta sobre el eje Y")  
elif xx == 0.0  and yy == 0.0:
        print("La coordenada",(xx, yy),"corresponde al origen")
#for quadrants
if xx > 0.0 and yy > 0.0:
    print("La coordenada",(xx, yy),"se encuentra en el cuadrante 1")
    
elif xx < -0.0 and yy > 0.0:
    print("La coordenada",(xx, yy),"se encuentra en el cuadrante 2")
elif xx< -0.0 and yy < -0.0:
    print("La coordenada",(xx, yy),"se encuentra en el cuadrante 3")
    
elif xx> 0.0 and yy< -0.0:
    print("La coordenada",(xx, yy),"se encuentra en el cuadrante 4")

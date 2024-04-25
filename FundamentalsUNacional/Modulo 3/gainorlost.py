startUp = int(input())
return1 = int(input())
equation1 = ((return1-startUp)/startUp)*100

if return1>startUp:
    
    print("Hubo una ganancia de $",return1-startUp,"correspondiente al",equation1,"% del capital invertido")
elif return1<startUp:
    
    print("Hubo una perdida de $",startUp-return1,"correspondiente al",equation1*-1,"% del capital invertido")
else:
    print("No hubo ni ganancia ni perdida, la inversion fue un desperdicio de tiempo, pero al menos no de dinero")
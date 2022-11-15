#ejercicio de la relatividad 
#string y archivos 
#hacer una funcion que reciba los valores de la formula y lo imprima 


import math 

lista = []
tranformacion = []

def inputs(): #hacer una funcion que si pongo un numero input pues se ejecute tres veces 
    request = int(input())
    while request>0:
      j = float(input())
      lista.append(j)
      request -= 1
      

inputs()


def conversion():
  
  for i in lista:
    veige = i/3.6
    tranformacion.append(veige)
    


conversion()

def formula(): #primero empiezo con la formula
  v=33.3333 #es la vista del observador #convertir de k/h a m/s
  c=299792458 #c es igual a la velocidad de la luz #ya esta convertida a m/s
  for i in tranformacion:
    r = 1/math.sqrt(1-(i**2/c**2))
    print(round(r,15))

formula()


'''
Manejo de archivos 

Basicamente hay dos tipos en el tema de Direccionamiento
y es el 
 - absoluto     este es aquel que me permite tomar la direccion ip del computador 
 - relativo     es maso menos que no esta en el pc si no en otra base de datos como podria ser la nube o otro servidor


'''
#este va a ser el metodo absoluto 
#stack overflow dice que no toma la ruta correcta porque lo toma como un string entonce hay que agregarle la r para  que lo tome como un string crudo
agregar = "Voy a ser el mejor programador en mi campo, e ire a canada a aumentar mi experiencia"
with open(r"C:\Users\andre\Desktop\mision_tic_retos\practice_for_exercise_fifth\archivos_que_voy_a_manejarXD.py\texto_que_saluda.txt", "r+") as f:
   f.write(agregar)   #este cambio se ve reflejado en el texto que modificamos 😳

#creamos otro archivo porque este me da una explicacion pero hay una mas interesante adelante 
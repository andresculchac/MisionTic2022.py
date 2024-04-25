'''
esto es lo que hace es agregar mas archivos con el comando "a"
'''

with open(r"C:\Users\andre\Desktop\mision_tic_retos\practice_for_exercise_fifth\archivos_que_voy_a_manejarXD.py\texto_que_saluda.txt", "a") as f:
    data = "me gusta las sandia\n"   #la diferencia entre "a" y "r+" es que si r+ ya esta en una sola variable vuelve y lo reeescribe 
    f.write(data)
    f.write(data)

#y si existe lo vuelve agregar

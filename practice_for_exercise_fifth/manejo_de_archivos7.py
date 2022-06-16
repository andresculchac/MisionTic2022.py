import json
'''
Tratamiento de datos para la base json del las sedes del Putumayo

'''

with open(r"C:\Users\andre\Desktop\mision_tic_retos\practice_for_exercise_fifth\archivos_que_voy_a_manejarXD.py\sedes_putumayo.json", encoding="utf8") as f:
    data = json.load(f)
    print("Type:", type(data))
    print(data)
    print("Type:", type(data))
    # no entiendo la parte en que tuvimos que pasar el json validator para que diera un diccionario si no antes era una lista 
    #por lo visto no todos los json son dict 




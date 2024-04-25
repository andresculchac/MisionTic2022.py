# '''
# I learned the difference between dumps and dump
# '''

#subject Dump 
import json

import json

with open(r"C:\Users\andre\Desktop\mision_tic_retos\practice_for_exercise_fifth\archivos_que_voy_a_manejarXD.py\states.json") as f:
    data = json.load(f) #segun lo entendido load sirve como para leer archivos y tambien pues esta leyendo archivos json que no se tiene que tener en cuenta 

for state in data['states']:
    print(state['name'], state['abbreviation'])
    
for states in data['states']:
    del states['name']


with open(r"C:\Users\andre\Desktop\mision_tic_retos\practice_for_exercise_fifth\archivos_que_voy_a_manejarXD.py\new_states.json", 'w') as f:
    json.dump(data, f)



# with open(r"C:\Users\andre\Desktop\mision_tic_retos\practice_for_exercise_fifth\archivos_que_voy_a_manejarXD.py\states.json","w")as f:
#     data = json.load(f)
    
# for state in data['states']:
#     del(state["area_codes"])

# with open(r"C:\Users\andre\Desktop\mision_tic_retos\practice_for_exercise_fifth\archivos_que_voy_a_manejarXD.py\new_states.json","w")as f:
#     json.dump(data, f)
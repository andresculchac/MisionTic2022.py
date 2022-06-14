'''
I learned between difference load and loads
Subjet : Load
'''
import json

with open(r"C:\Users\andre\Desktop\mision_tic_retos\practice_for_exercise_fifth\archivos_que_voy_a_manejarXD.py\states.json") as f:
    data = json.load(f) #segun lo entendido load sirve como para leer archivos 

for state in data['states']:
    print(state['name'], state['abbreviation'])
    
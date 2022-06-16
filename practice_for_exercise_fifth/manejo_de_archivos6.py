'''
I learned between difference load and loads
Subjet : Load
'''
import json

with open(r"C:\Users\andre\Desktop\mision_tic_retos\practice_for_exercise_fifth\archivos_que_voy_a_manejarXD.py\states.json") as f:
    data = json.load(f) #segun lo entendido load sirve como para leer archivos y tambien pues esta leyendo archivos json que no se tiene que tener en cuenta 
    print(type(data))
for state in data['states']:
    print(state['name'], state['abbreviation'])
    
for states in data['states']:
    del states['area_codes'] 
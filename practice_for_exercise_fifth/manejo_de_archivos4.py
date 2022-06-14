import json

familia =  {
    "mama":True,
    "papa": None
}

print(json.dumps(familia,indent=40))



#dump lo que hace es convertir de diccionario a json hace como una serializacion o algo asi 
#y pues loads es como lo contrario 
'''
import request 
Subject API 
api es una base de datos que podemos consultarla a internet y esto re relacion con ser un dato relativo 


'''
import json
import requests
import pprint
raza = input("digite una raza de perrro ")
url = "https://dog.ceo/api/breed/"+raza+"/images/random"

print(url)
respuesta = requests.get(url)
pprint.pprint(json.loads(respuesta.text))


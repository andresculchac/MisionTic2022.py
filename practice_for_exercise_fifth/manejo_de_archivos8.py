'''
import request 
Subject REQUEST 
es como una solicitud a un  servidor
y retorna algo 
esa respuesta es conocida como un respond 

response 200 si existe todo bien todo correcto
response 400 error 
'''
import json
import requests
url = "https://www.datos.gov.co/resource/gt2j-8ykr.json"
respuesta = requests.get(url)
print(type(json.loads(respuesta.text)))







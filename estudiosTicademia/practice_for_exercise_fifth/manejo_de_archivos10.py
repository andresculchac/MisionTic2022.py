import requests as req
import json
import pprint
import matplotlib.pyplot as plt
from skimage import io
raza        = input("Digite una raza de perro")
url         = "https://dog.ceo/api/breed/"+raza+"/images/random"
respuesta   = req.get(url)
diccionario = json.loads(respuesta.text)
imagen      = diccionario["message"]
image       = io.imread(imagen)
plt.imshow(image)
plt.xticks([])
plt.yticks([])
plt.show()
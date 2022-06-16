'''
Para ayudar a Marta y María, se le pide a usted hacer un módulo en Python con nombre productos.py que va a ser usado por otros programadores y que debe tener como mínimo las siguientes funciones:

1. La función “grupos” que dada una lista en donde se muestra los grupos de cada producto (cada posición i de la lista es el grupo del producto i), genera una lista con los grupos únicos existentes. Por ejemplo, si se recibe una lista como la siguiente:

 

[“verduras”,”verduras”,”granos”,”granos”,”verduras”,”frutas”,”frutas”,”carnes”,”carnes”] -> Lista de grupos

 

Devuelve:

[“verduras”,”granos”,”frutas”,”carnes”] -> Lista de grupos únicos
'''


def grupos(grupos):
  grup = []
  for dato in grupos:
    if dato not in grup:
      grup.append(dato)
  return grup

def necesito_del_grupo(indices,lgrupos,grupos):
  grup = []
  return grup

def sirven_a_marta(productos_maria, productos_marta):
  grup = []
  return grup

def cuantas_cambian(productos_maria, productos_marta):
  cantidad = 0
  return cantidad





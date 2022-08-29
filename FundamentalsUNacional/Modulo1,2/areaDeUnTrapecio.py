#las separaciones con decimales en python se hacen con puntos y no con comas OJO
#no podemos sumar float + string por eso esta la coma 
B, b, h = float(input()), float(input()), float(input())
print('El lote tiene',(((B+b)*h)/2),"metros cuadrados")
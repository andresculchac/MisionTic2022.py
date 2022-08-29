#las separaciones con decimales en python se hacen con puntos y no con comas OJO
#no podemos sumar float + string por eso esta la coma 
#si ya se tiene un float en input ya no es necesario pues el float en print
B, b, h = float(input()), float(input()), float(input())
print('El lote tiene',(((B+b)*h)/2),"metros cuadrados")

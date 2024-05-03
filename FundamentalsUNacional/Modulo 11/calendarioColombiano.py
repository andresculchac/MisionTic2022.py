import datetime 

# matrix =[["lun\t","mar\t","mie\t","jue\t","vie\t","sab\t","dom"],
#          ["\t",2,3,4,5,6]]

# #"10/02/2010"
# #dia, mes,  año

# for row in matrix:
#     for element in row:
#         print(element, end=" ")
#     print()


from datetime import datetime

# Crear un objeto de fecha para el 1 de enero de 2010
fecha = datetime(2010, 1, 1)

# Obtener el día de la semana (0 para lunes, 1 para martes, ..., 6 para domingo)
dia_semana = fecha.weekday()

# Lista de nombres de los días de la semana
nombres_dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

# Imprimir el día de la semana en que cae el 1 de enero de 2010
print("El 1 de enero de 2010 cae en", nombres_dias_semana[dia_semana])




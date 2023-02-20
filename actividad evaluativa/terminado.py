mm1 = []
mm2 = []

m1_temp = []
m2_temp = []

dim1 = input()
dim2 = input()

ldim1 = dim1.split('x')
ldim2 = dim2.split('x')

fm1 = int(ldim1[0])
cm1 = int(ldim1[1])

fm2 = int(ldim2[0])
cm2 = int(ldim2[1])

num_m1 = fm1*cm1
num_m2 = fm2*cm2

if cm1 != fm2:
    print("Las columnas de la primera tabla deben ser iguales a las filas de la segunda tabla")

else:
    for j in range(0,num_m1):
        m1 = input()
        m1 = int(m1)
        m1_temp.append(m1)
        #print("ENTRADA", m1_temp)
        #print("LEN ",len(m1_temp))
        if len(m1_temp) == cm1:
            mm1.append(m1_temp)
            m1_temp = []

    for j in range(0,num_m2):
        m2 = input()
        m2 = int(m2)
        m2_temp.append(m2)
        #print("ENTRADA", m1_temp)
        #print("LEN ",len(m1_temp))
        if len(m2_temp) == cm2:
            mm2.append(m2_temp)
            m2_temp = []

print(mm1)
print(mm2)

"""print("MATRIZ ", mm1)  
    print("MATRIZ ", mm2)"""

    # m_t= [[0]*fm1]*cm2
    # multi = 0

    # for fila in range(fm1):
    #     linea=""
    #     for columna in range(cm2):
    #       aux=0
    #       for e in range(cm1):
    #         r_temp=mm1[fila][e]*mm2[e][columna]
    #         aux+=r_temp        
    #       linea+= str(aux)+" "
    #     print(linea[:-1])
    #print(multi)
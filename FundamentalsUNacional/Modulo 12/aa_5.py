from collections import defaultdict
second_life = []
#init form
init_form  = defaultdict(lambda:0)
with open('discurso.txt', 'r') as fichero: 
    for ix in fichero: # relacion con modulo 9
        discursos = []
        for mx in ix.lower().replace('.','').replace(',','').replace('?','').replace(';','').replace(':','').split():
            form = []
            if len(mx)>4:
                if mx not in second_life: second_life.append(mx)
                if mx not in discursos: discursos.append(mx)
        for col in discursos: init_form[col] += 1               
for sort_init in sorted(second_life):
    print(f'{sort_init} {init_form[sort_init]}')
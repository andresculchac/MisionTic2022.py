from collections import defaultdict
cleaner_discurso = []
#init form
final_disc  = defaultdict(lambda:0)
with open('discurso.txt', 'r') as fichero: 
    for ix in fichero: # relacion con modulo 9
        discursos = []
        for mx in ix.lower().replace('.','').replace(',','').replace('?','').replace(';','').replace(':','').split():
            form = []
            if len(mx)>4:
                if mx not in cleaner_discurso: cleaner_discurso.append(mx)
                if mx not in discursos: discursos.append(mx)
        for col in discursos: final_disc[col] += 1               
for sort_init in sorted(cleaner_discurso):
    print(f'{sort_init} {final_disc[sort_init]}')
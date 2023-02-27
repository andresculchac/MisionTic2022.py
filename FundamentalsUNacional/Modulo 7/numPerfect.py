perfecteds=[]


def vine(x):
	xx = 0
	for perf in range(1,x):
		if (x % (perf) == 0):
			xx += (perf)
	if x == xx:
		return True
	else:
		return False


hiv=int(input())
while hiv>0:
  nice=int(input())
  perfecteds.append(nice)
  hiv-=1

  
for lil in perfecteds:
	if vine(lil)==True:
		print(lil,"es perfecto")
	else:
		print(lil,"no es perfecto")
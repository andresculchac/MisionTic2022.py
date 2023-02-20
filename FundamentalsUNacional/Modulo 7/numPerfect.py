l=[]
def f_1(x):
	suma = 0
	for i in range(1,x):
		if (x % (i) == 0):
			suma += (i)
	if x == suma:
		return True
	else:
		return False

m=int(input())
while m>0:
  m_1=int(input())
  l.append(m_1)
  m-=1
for i in l:
	if f_1(i)==True:
		print(i,"es perfecto")
	else:
		print(i,"no es perfecto")
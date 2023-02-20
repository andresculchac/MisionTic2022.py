def panaderia(x):
  panzote=(5*x+4)**0.5
  return panzote

def sinergia(x):
  xx=3**x
  return xx
def mina(x):
  vv=2*x+1
  return vv

#ultimo intento 
sinergya=int(input())

while sinergya>0:
  panzote=(mina(sinergia(panaderia(float(input())))))
  sinergya-=1

  print(panzote)
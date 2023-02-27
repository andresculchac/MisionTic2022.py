#clear Msg
def msg(inpt):
    simp = ""
    for nobody in inpt:
        simp = nobody + simp
    return simp

clear=open('mensaje.txt',"r")
#Inicio for msg 
for ix in clear:
  ix=ix.replace("\n","")
  msg_clear=msg(ix)
  print(msg_clear)
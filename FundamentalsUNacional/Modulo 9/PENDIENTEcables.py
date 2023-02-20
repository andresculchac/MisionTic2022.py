l=[]
m=int(input())
while m>0:
  c=input().split()
  f=0
  m=0
  for dupla in c:
    if dupla[0]=="F":
      f+=1
    else:
      m+=1
    if dupla[1]=="F":
      f+=1
    else:
      m+=1
  if m==f:
    print("ES")
  else:
    print("no")
  m-=1
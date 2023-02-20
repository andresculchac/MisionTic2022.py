l=[]
def fa(n): 
    if(n == 0 or n == 1): 
        fa = 1
    else: 
        fa = n*fa(n - 1) 
    return fa 
  
def s_n(x): 
    n_l =[] 
    for i in x: 
        temp = i
        sum = 0
        while(temp): 
            rem = temp % 10
            sum += fa(rem) 
            temp = temp // 10
        if(sum == i): 
            n_l.append(i) 
        else: 
            pass  
    return n_l 

m=int(input())
while m>0:
  m_1=int(input())
  l.append(m_1)
  m-=1

s_n_l = s_n(l)
#for i in s_n_l:
for j in l:
    if j in s_n_l:
      print(j,"es fuerte")
    else:
      print(j,"no es fuerte")
      #preguntar el print
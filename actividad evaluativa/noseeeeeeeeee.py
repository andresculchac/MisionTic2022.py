
entrada = input()
entrada2 = input()

inputPrincipal = []
InputPrincipal2 = []

birl = []
birl2 = []

string = entrada.split('x')
separate = entrada2.split('x')

list1 = int(string[0])
list2 = int(string[1])
list3 = int(separate[0])
list4 = int(separate[1])

num_m1 =list1*list2
num_m2 = list3*list4

for j in range(num_m1):
        m1 = int(input())      
        birl.append(m1)   
        if len(birl) == list2:
            inputPrincipal.append(birl)
            birl = []

for j in range(num_m2):
        m2 = int(input())
        birl2.append(m2)
        if len(birl2) == list4:
            InputPrincipal2.append(birl2)
            birl2 = []





print(inputPrincipal)
print(InputPrincipal2)
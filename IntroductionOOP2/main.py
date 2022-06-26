

from Employee import Employee
from Customer import Customer



emp = Employee('Patty', 'Chapid', '6698948', '3123239153', 1000)
cli = Customer('Patty', 'Chapid', '6698948', '3123239153', 'vip')



def loadLoading():
    reply = input('You add an employee?')
    name = input('input their name')
    surname = input('input their surname')
    dni = input('input their dni')
    telephone = input('input their phone number')



    if (reply == 'yes'):
        salary = input('input their salary')
        emp = Employee(name,surname,dni,telephone, int(salary))
        people.append(emp)
        

    else:
        type = input('input the type of customer')
        cli = Employee(name,surname,dni,telephone, type)
        people.append(cli)
        
people = []
loadLoading()
loadLoading()

for i in people:
    print(i)




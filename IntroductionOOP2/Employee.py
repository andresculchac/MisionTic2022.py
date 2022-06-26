from Person import Person

class Employee(Person):
    def __init__(self, name, surname, dni, telephone,salary):
        super().__init__(name, surname, dni, telephone)
        self.salary = salary
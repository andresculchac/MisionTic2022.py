from Person import Person

class Customer(Person):
    def __init__(self, name, surname, dni, telephone, category):
        super().__init__(name, surname, dni, telephone)
        self.category = category
    
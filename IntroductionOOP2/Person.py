class Person:
    def __init__(self, name, surname, dni, telephone):
        self.name = name
        self.surname = surname
        self.dni = dni
        self.telephone = telephone

    def __str__(self) -> str:     #In summary i can return an abstract representation of the def
        return self.name + ' ' + self.surname


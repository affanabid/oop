class Human:
    def __init__(self, name) -> None:
        self.name = name

class Boss(Human):
    def __init__(self, name, age) -> None:
        super().__init__(name)
        self.age = age

    def add_age(self, no):
        self.age += no 

class Employee(Human):
    def __init__(self, name, code='', position='') -> None:
        super().__init__(name)
        self.code = code
        self.position = position

class Person(Boss, Employee):
    def __init__(self, name, age, code, position) -> None:
        super().__init__( name, age)
        super().__init__(self, name, code, position)

person = Person('Affan', 20, 9, 'Developer')

print(person)
# person.add_age(5)
# print(person.age)
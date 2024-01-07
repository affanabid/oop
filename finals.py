class Human:
    def __init__(self, name , age) -> None:
        self.name = name
        self.age = age

    def add_age(self, no):
        self.age += no 

class Employee:
     def __init__(self, code, position) -> None:
          self.code = code
          self.position = position

class Person(Human, Employee):
     def __init__(self, name, age, code, position) -> None:
          Human.__init__(self, name, age)
          Employee.__init__(self, code, position)

person = Person('Affan', 20, 9, 'Developer')
print(person.age)
person.add_age(5)
print(person.age)
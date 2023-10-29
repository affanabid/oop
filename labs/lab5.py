class Department:

    def __init__(self, name, chairman, id) -> None:
        self.__name = name
        self.chairman = chairman
        self.__id = id

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id = value
    # def get_name(self):
    #     return self.__name

    # def set_name(self, name):
    #     self.__name = name

    def department(self):
        return self.name
    
    def sep_chairman(self):
        return self.chairman

    def __str__(self) -> str:
        return f'Department: {self.__id}, {self.__name}, {self.chairman}'

class Student:

    def __init__(self, name, rollno, sem, cgpa, dep_id):
        self.__name =  name
        self.rollno = rollno
        self.sem = sem
        self.cgpa = cgpa
        self.dep_id = dep_id

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    def roll(self):
        return self.rollno
    
    def semester(self):
        return self.sem
    
    def student_cgpa(self):
        return self.cgpa
    
    def __str__(self) -> str:
        return f'{self.rollno}\t\t{self.__name}\t\t\t{self.sem}\t\t{self.cgpa}'
    
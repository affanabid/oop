class Person:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def __str__(self) -> str:
        return f'\nName: {self.name}\tContact: {self.contact}'

class Student(Person):
    def __init__(self, name, contact, department='', semester=None):
        super().__init__(name, contact)
        self.department = department
        self.semester = semester
    
    def __str__(self) -> str:
        return f'\nName: {self.name}\tContact: {self.contact}\tDepartment: {self.department}\tSemester: {self.semester}'

class Teacher(Person):
    def __init__(self, name, contact, course, office_number):
        super().__init__(name, contact)
        self.course = course
        self.office_number = office_number
    
    def __str__(self) -> str:
        return f'\nName: {self.name}\tContact: {self.contact}\tCourse: {self.course}\tOffice no.: {self.office_number}'

class TA(Teacher, Student):
    def __init__(self, name, contact, department, semester, course, office_number):
        Teacher.__init__(self, name=name, contact=contact, course=course, office_number=office_number)
        Student.__init__(self, name=name, contact=contact, department=department, semester=semester)

    def __str__(self):
        return f"\nName: {self.name}\tContact: {self.contact}\tDepartment: {self.department}\t" \
               f"Semester: {self.semester}\tCourse: {self.course}\tOffice Number: {self.office_number}"

ta = TA("Affan Abid", "1234567890", "Data Science", 3, "Python", 101)
print('TA: ',ta)

person = Person('ali', '0')
print('Person: ',person)

student = Student('Ahmad', '03009876234', 'Software Engineering', 5)
print('Student: ',student)

teacher = Teacher('Imtiaz', '03009876234', 'Calculus', 10)
print('Teacher: ',teacher)
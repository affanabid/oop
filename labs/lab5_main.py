from lab5 import Department, Student

cs_department = Department('Computer Science', 'Dr. Jodat Kamal', 'CS')
it_department = Department('Information Technology', 'Dr. Sodat Kamal', 'IT')
se_department = Department('Softwaree Engineering', 'Dr. Rodat Kamal', 'SE')
ds_department = Department('Data Science', 'Dr. Nodat Kamal', 'DS')

cs_students = [
    Student('Ahmad', 'cs001', '1', '3.5', 'CS'),
    Student('Ali', 'cs002', '2', '1.1', 'CS'),
    Student('Umar', 'cs003', '3', '3.3', 'CS'),
]

it_students = [
    Student('Ahmad', 'it001', '1', '1.5', 'IT'),
    Student('Hadi', 'it002', '2', '3.4', 'IT'),
    Student('Irtiza', 'it003', '3', '3.3', 'IT'),
]

se_students = [
    Student('Qazim', 'se001', '1', '3.5', 'SE'),
    Student('Waleed', 'se002', '2', '1.4', 'SE'),
    Student('Asim', 'se003', '3', '3.3', 'SE'),
]

ds_students = [
    Student('Ahmad', 'ds001', '1', '3.5', 'DS'),
    Student('Amir', 'ds002', '2', '3.4', 'DS'),
    Student('Usman', 'ds003', '3', '1.3', 'DS'),
]

failed = []

print(cs_department)
print(f'Roll No.\tName\t\t\tSemester\tCGPA')
for student in cs_students:
    if float(student.cgpa) < 1.7:
        failed.append(student)
    print(student)
print()

print(it_department)
print(f'Roll No.\tName\t\t\tSemester\tCGPA')
for student in it_students:
    if float(student.cgpa) < 1.7:
        failed.append(student)
    print(student)
print()

print(se_department)
print(f'Roll No.\tName\t\t\tSemester\tCGPA')
for student in se_students:
    if float(student.cgpa) < 1.7:
        failed.append(student)
    print(student)
print()

print(ds_department)
print(f'Roll No.\tName\t\t\tSemester\tCGPA')
for student in ds_students:
    if float(student.cgpa) < 1.7:
        failed.append(student)
    print(student)
print()

print('Students with cgpa less than 1.7:')
print(f'Roll No.\tName\t\t\tSemester\tCGPA')
for failure in failed:
    print(failure)
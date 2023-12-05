import struct

grades_struct = struct.Struct('20s11sf')
student_struct = struct.Struct('11s30s2sif11s')

def add_from_file():    
    with open('grds.txt', 'r') as file:
        lines = file.readlines()
        print(lines)
        for line in lines:
            data = line.split()
            data[2] = float(data[2])
            add_grades(data)

def add_grades(data):
    course = bytes(data[0], 'utf-8')
    roll_no = bytes(data[1], 'utf-8')
    perc = data[2]
    if valid_course(data[1], data[0]):
        with open('grades.bin', 'ab+') as file:
            byte = grades_struct.pack(course, roll_no, perc)
            file.write(byte)
            file.write(b'\n')
            print('Grade data added')
    else:
        print('Grade already exists')
def valid_course(roll_no, course):
    with open('grades.bin', 'rb') as file:
        lines = file.readlines()
        for line in lines:
            data = struct.unpack('20s11sf1s', line)
            data_roll_no = data[1].decode().strip('\x00')
            data_course = data[0].decode().strip('\x00')
            if roll_no == data_roll_no and data_course == course:
                return False
    return True

def add_student_from_file():    
    with open('std.txt', 'r') as file:
        lines = file.readlines()
        print(lines)
        for line in lines:
            data = line.split()
            data[3] = int(data[3])
            data[4] = float(data[4])
            add_student(data)

def add_student(data):
    roll_no = bytes(data[0], 'UTF-8')
    name = bytes(data[1], 'UTF-8')
    dept = bytes(data[2], 'UTF-8')
    sem = data[3]
    perc = data[4]
    phone = bytes(data[5], 'UTF-8')
    if valid_entry(data[0], data):
        with open('std.bin', 'ab+') as file:
            byte = student_struct.pack(roll_no, name, dept, sem, perc, phone)
            file.write(byte)
            file.write(b'\n')
            print('Student data added')
    else:
        print('Student data already present')

def valid_entry(roll_no, data):
    with open('std.bin', 'rb') as file:
        entries = file.readlines()
        for entry in entries:
            data = struct.unpack('11s30s2sif11s1s', entry)
            data_roll_no = data[0].decode()
            if roll_no == data_roll_no:
                return False
    return True
# add_student_from_file()
add_from_file()
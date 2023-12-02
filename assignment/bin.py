import pickle, struct

student_struct = struct.Struct('11s30s2sif11s')

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
# add_student(['BSDSF22A012', 'AFRAM', 'DS', 2, 90.5, '03001234567'])

def delete_student(req_roll_no):
    with open('std.bin', 'r+b') as file:
        lines = file.readlines()
        # file.seek(0)
    with open('std.bin', 'wb') as file2:
        for line in lines:
            data = struct.unpack('11s30s2sif11s1s', line)
            roll_no = data[0].decode()
            if req_roll_no != roll_no:
                file2.write(line)
    print('Deleted Successfully')
# delete_student('BSDSF22A014')

def view_student(req_roll_no):
    with open('std.bin', 'rb') as file:
        entries = file.readlines()
        for entry in entries:
            data = struct.unpack('11s30s2sif11s1s', entry)
            roll_no = data[0].decode()
            if roll_no == req_roll_no:
                read_bytes(data)

def read_bytes(data):
    for element in data:
        if isinstance(element, int):
            print(element, end=' ')
        elif isinstance(element, float):
            print(element, end=' ')
        else:
            print(element.decode(), end=' ')
    print()
# view_student('BSDSF22A011')
# view_student('BSDSF22A010')

def student_list():
    with open('std.bin', 'rb') as file:
        entries = file.readlines()
        for entry in entries:
            print(entry)
# new_byte = student_struct.unpack(byte)
#     print(new_byte[0].decode('utf-8'))

def add_grades(roll_no, grade, course):
    with open(f'{course}.bin', 'ab+') as file:
        roll_no = bytes(roll_no, 'utf-8')
        grade = bytes(grade, 'utf-8')
        file.write(roll_no)
        file.write(b'\t')
        file.write(grade)
        file.write(b'\n')
add_grades('BSDSF22A012', 'A', 'pf')
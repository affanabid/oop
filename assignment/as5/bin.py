import struct

student_struct = struct.Struct('11s30s2sif11s')
grades_struct = struct.Struct('20s11sf')

# 2. Add a student and check for duplicates
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

# 3. View student by roll no
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

# 4. Edit student by Roll No
def edit_student(roll_no):
    user = input("What do you want to update?\ns)semester, d) department, p) Percentage, c) Contact No.\n")
    if user == 's':
        sem = input('Enter new semester: ')
        edit_student_sem(req_roll_no=roll_no,new_sem=sem)
    elif user == 'd':
        dept = input('Enter new department: ')
        edit_student_dept(req_roll_no=roll_no, new_dept=dept)
    elif user == 'p':
        perc = input('Enter new percentage: ')
        edit_student_perc(req_roll_no=roll_no, new_perc=perc)
    elif user == 'c':
        contact = input('Enter new contact: ')
        edit_student_phone(req_roll_no=roll_no, new_phone=contact)
    else:
        print('Enter valid input')

def edit_student_sem(req_roll_no, new_sem):
    with open('std.bin', 'rb') as file:
        lines = file.readlines()
    with open('std.bin', 'wb') as file2:
        for line in lines:
            data = struct.unpack('11s30s2sif11s1s', line)
            roll_no = data[0].decode()
            if req_roll_no == roll_no:
                roll_no = bytes(roll_no, 'UTF-8')
                name = bytes(data[1].decode(), 'UTF-8')
                dept = bytes(data[2].decode(), 'UTF-8')
                sem = int(new_sem)
                perc = data[4]
                phone = bytes(data[5].decode(), 'UTF-8')
                byte = student_struct.pack(roll_no, name, dept, sem, perc, phone)
                file2.write(byte)
                file2.write(b'\n')
            else:
                file2.write(line)
    print('Student Semester Updated')

def edit_student_dept(req_roll_no, new_dept):
    with open('std.bin', 'rb') as file:
        lines = file.readlines()
    with open('std.bin', 'wb') as file2:
        for line in lines:
            data = struct.unpack('11s30s2sif11s1s', line)
            roll_no = data[0].decode()
            if req_roll_no == roll_no:
                roll_no = bytes(roll_no, 'UTF-8')
                name = bytes(data[1].decode(), 'UTF-8')
                dept = bytes(new_dept, 'UTF-8')
                sem = data[3]
                perc = data[4]
                phone = bytes(data[5].decode(), 'UTF-8')
                byte = student_struct.pack(roll_no, name, dept, sem, perc, phone)
                file2.write(byte)
                file2.write(b'\n')
            else:
                file2.write(line)
    print('Student Department Updated')

def edit_student_perc(req_roll_no, new_perc):
    with open('std.bin', 'rb') as file:
        lines = file.readlines()
    with open('std.bin', 'wb') as file2:
        for line in lines:
            data = struct.unpack('11s30s2sif11s1s', line)
            roll_no = data[0].decode()
            if req_roll_no == roll_no:
                roll_no = bytes(roll_no, 'UTF-8')
                name = bytes(data[1].decode(), 'UTF-8')
                dept = bytes(data[2].decode(), 'UTF-8')
                sem = data[3]
                perc = new_perc
                phone = bytes(data[5].decode(), 'UTF-8')
                byte = student_struct.pack(roll_no, name, dept, sem, perc, phone)
                file2.write(byte)
                file2.write(b'\n')
            else:
                file2.write(line)
    print('Student Percentage Updated')

def edit_student_phone(req_roll_no, new_phone):
    with open('std.bin', 'rb') as file:
        lines = file.readlines()
    with open('std.bin', 'wb') as file2:
        for line in lines:
            data = struct.unpack('11s30s2sif11s1s', line)
            roll_no = data[0].decode()
            if req_roll_no == roll_no:
                roll_no = bytes(roll_no, 'UTF-8')
                name = bytes(data[1].decode(), 'UTF-8')
                dept = bytes(data[2].decode(), 'UTF-8')
                sem = data[3]
                perc = data[4]
                phone = bytes(new_phone, 'UTF-8')
                byte = student_struct.pack(roll_no, name, dept, sem, perc, phone)
                file2.write(byte)
                file2.write(b'\n')
            else:
                file2.write(line)
    print('Student Phone No. Updated')

# 5. Delete student by roll no
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

# 6. List student by semester
def list_student_by_sem(req_sem):
    with open('std.bin', 'rb') as file:
        entries = file.readlines()
        for entry in entries:
            data = struct.unpack('11s30s2sif11s1s', entry)
            sem = data[3]
            if sem == req_sem:
                read_bytes(data)

# 7. List student by name
def list_student_by_name(req_name):
    with open('std.bin', 'rb') as file:
        entries = file.readlines()
        for entry in entries:
            data = struct.unpack('11s30s2sif11s1s', entry)
            name = data[1].decode().strip('\x00')
            if name == req_name:
                read_bytes(data)

# 8. Print Students list
def student_list():
    print('Roll No.\tName\tDept\tSem\tmarks\tContact')
    with open('std.bin', 'rb') as file:
        entries = file.readlines()
        for entry in entries:
            data = struct.unpack('11s30s2sif11s1s', entry)
            roll_no = data[0].decode()
            name = data[1].decode()
            dept = data[2].decode()
            sem = data[3]
            perc = data[4]
            contact = data[5].decode()
            print(f'{roll_no}\t{name}\t{dept}\t{sem}\t{perc}\t{contact}')

# 9. Add grade for a course and check for duplicates
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

# 10. Import grades for a course from grds.txt file
def add_from_file():    
    with open('grds.txt', 'r') as file:
        lines = file.readlines()
        print(lines)
        for line in lines:
            data = line.split()
            data[2] = float(data[2])
            add_grades(data)

# 11. View grades of a student
def view_grade_sw(req_roll_no):
    with open(f'grades.bin', 'rb') as file:
        lines = file.readlines()
        search = False
        print(f'Student: {req_roll_no}')
        for line in lines:
            data = struct.unpack('20s11sf1s', line)
            roll_no = data[1].decode()
            if roll_no == req_roll_no:
                print(f'\nCourse: {data[0].decode()}\nMarks: {data[2]}\nGrade: {assign_grade(data[2])}')
                search = True
    if search == False:
        print('Student not found')

def assign_grade(score):
    if score >= 85:
        return "A+"
    elif 80 <= score < 85:
        return "A-"
    elif 75 <= score < 80:
        return "B+"
    elif 70 <= score < 75:
        return "B"
    elif 65 <= score < 69:
        return "B-"
    elif 61 <= score < 65:
        return "C+"
    elif 58 <= score < 61:
        return "C"
    elif 55 <= score < 57:
        return "C-"
    elif 50 <= score < 55:
        return "D"
    else:
        return "F"
    
# 12. Edit grades of a student for a course
def edit_grade(req_roll_no, req_course, new_marks):
    with open('grades.bin', 'rb') as file:
        lines = file.readlines()
    with open('grades.bin', 'wb') as file2:
        for line in lines:
            data = struct.unpack('20s11sf1s', line)
            roll_no = data[1].decode().strip('\x00')
            course = data[0].decode().strip('\x00')
            # print(course)
            if req_roll_no == roll_no and req_course == course:
                course = bytes(data[0].decode(), 'utf-8')
                roll_no = bytes(roll_no, 'UTF-8')
                perc = new_marks
                byte = grades_struct.pack(course, roll_no, perc)
                file2.write(byte)
                file2.write(b'\n')
            else:
                file2.write(line)
    print('Student grade Updated')

# 13. Delete grades of a student for a course
def delete_grade(req_roll_no, req_course):
    with open('grades.bin', 'r+b') as file:
        lines = file.readlines()
    with open('grades.bin', 'wb') as file2:
        for line in lines:
            data = struct.unpack('20s11sf1s', line)
            roll_no = data[1].decode().strip('\x00')
            course = data[0].decode().strip('\x00')
            if req_roll_no != roll_no or req_course != course:
                file2.write(line)
    print('Deleted Successfully')

# 14. List student wise grades of course
def view_grade_sw(req_roll_no):
    with open(f'grades.bin', 'rb') as file:
        lines = file.readlines()
        search = False
        print(f'Student: {req_roll_no}')
        for line in lines:
            data = struct.unpack('20s11sf1s', line)
            roll_no = data[1].decode()
            if roll_no == req_roll_no:
                print(f'\nCourse: {data[0].decode()}\nMarks: {data[2]}\nGrade: {assign_grade(data[2])}')
                search = True
    if search == False:
        print('Student not found')

# 15. List course wise grade of students
def view_grade_cw(req_course):
    with open(f'grades.bin', 'rb') as file:
        lines = file.readlines()
        search = False
        print(f'Course: {req_course}')
        for line in lines:
            data = struct.unpack('20s11sf1s', line)
            course = data[0].decode().strip('\x00')
            if course == req_course:
                print(f'\nStudent: {data[1].decode()}\nMarks: {data[2]}\nGrade: {assign_grade(data[2])}')

# 16. Award Sheet
def award_list():
    with open(f'grades.bin', 'rb') as file:
        lines = file.readlines()
        course = 'PF'
        print('Course: ',course)
        for line in lines:
            data = struct.unpack('20s11sf1s', line)
            data_course = data[0].decode().strip('\x00')
            if course == data_course:
                print(f'Student: {data[1].decode()}\tPercentage: {data[2]}\tGrade: {assign_grade(data[2])}')
        course = 'OOP'
        print('\nCourse: ',course)
        for line in lines:
            data = struct.unpack('20s11sf1s', line)
            data_course = data[0].decode().strip('\x00')
            if course == data_course:
                print(f'Student: {data[1].decode()}\tPercentage: {data[2]}\tGrade: {assign_grade(data[2])}')
        course = 'DLD'
        print('\nCourse: ',course)
        for line in lines:
            data = struct.unpack('20s11sf1s', line)
            data_course = data[0].decode().strip('\x00')
            if course == data_course:
                print(f'Student: {data[1].decode()}\tPercentage: {data[2]}\tGrade: {assign_grade(data[2])}')

# 17. Summary Sheet
def summary_sheet():
    print('ROLL NO\t\tNAME\tDEPT\tSEM\tPERC\tCONTACT\t\tCRS: PERC\tCRS: PERC\tCRS: PERC')

    with open('std.bin', 'rb') as file1:
        student_data = file1.readlines()
        for student in student_data:
            data = struct.unpack('11s30s2sif11s1s', student)
            roll_no = data[0].decode()
            name = data[1].decode()
            dept = data[2].decode()
            sem = data[3]
            perc = data[4]
            contact = data[5].decode()
            print(f'{roll_no}\t{name}\t{dept}\t{sem}\t{perc}\t{contact}', end='\t')

            with open('grades.bin', 'rb') as file2:
                grades_data = file2.readlines()
                for grade in grades_data:
                    g_data = struct.unpack('20s11sf1s', grade)

                    
                    g_roll_no = g_data[1].decode()
                    if roll_no == g_roll_no:
                        course = g_data[0].decode()
                        perc = g_data[2]
                        print(f'{course}: {perc}', end='\t')
            print()

# 18. Transcripts for a range of Students
def transcript(start, end):
    roll_list = []
    if start > 0 and end < 10:
        while start <= end:
            roll_no = 'BSDSF22A00' + str(start)
            roll_list.append(roll_no)
            start += 1
    else:
        print('Invalid Input!')
    view_transcript(roll_list)

def view_transcript(roll_no):
    for req_roll_no in roll_no:
        with open('std.bin', 'rb') as file1:
            student_data = file1.readlines()
            for student in student_data:
                data = struct.unpack('11s30s2sif11s1s', student)
                s_roll_no = data[0].decode()
                if s_roll_no == req_roll_no:
                    name = data[1].decode().strip('\x00')
                    dept = data[2].decode().strip('\x00')
                    sem = data[3]
                    perc = data[4]
                    contact = data[5].decode().strip('\x00')

                    print(f'{s_roll_no}\t{name}\t{dept}\t{sem}\t{perc}\t{contact}', end='\t')

                    with open('grades.bin', 'rb') as file2:
                        grades_data = file2.readlines()
                        for grade in grades_data:
                            g_data = struct.unpack('20s11sf1s', grade)
                            g_roll_no = g_data[1].decode()
                            if s_roll_no == g_roll_no:
                                course = g_data[0].decode().strip('\x00')
                                perc = g_data[2]
                                print(f'{course}: {perc}', end='\t')

        print()

# main function to check all the functions through commands from 1 to 18
def main():
    user = 2
    while user != 1:
        user = int(input('Welcome to Management System.\nEnter any number to proceed one of following commands:\n1. QUIT the management system\n2. Add a student\n3. View student by roll no\n4. Edit student by roll no (check for NO duplicates)\n5. Delete student by roll no\n6. List student by semester\n7. List students by name\n8. Print students list\n9. Add grade of a student for a course (check for NO duplicates)\n10. Import grades for a course for many students from a TABed text file (NO DUPS)\n11. View grades of a student\n12. Edit grades of a student for a course (NO DUPS, SKIP IF TIME IS SHORT)\n13. Delete grades of a student for a course (SKIP IF TIME IS SHORT)\n14. List Student wise (1 student) grade of courses\n15. List Course wise grade (1 course) of students\n16. Award sheet (courses one by one, with students enrolled in it)\n17. Summary sheet (courses info, one by one, with one line for each student in it)\n18. Transcripts for a range of students\n'))
        if user == 2:
            roll_no = input('Enter Roll No: ')
            name = input('Enter Name: ')
            dept = input('Enter Department: ')
            sem = int(input('Enter Semester: '))
            perc = float(input('Enter Percentage: '))
            contact = input('Enter Contact no: ')
            add_student([roll_no, name, dept, sem, perc, contact])
        elif user == 3:
            roll_no = input('Enter Roll No: ')
            view_student(req_roll_no=roll_no)
        elif user == 4:
            roll_no = input('Enter Roll No: ')
            edit_student(roll_no=roll_no)
        elif user == 5:
            roll_no = input('Enter Roll No: ')
            delete_student(req_roll_no=roll_no)
        elif user == 6:
            sem = int(input('Enter Sem: '))
            list_student_by_sem(sem)
        elif user == 7:
            name = input('Enter a name: ')
            list_student_by_name(name)
        elif user == 8:
            student_list()
        elif user == 9:
            roll_no = input('Enter Roll No: ')
            course = input('Enter Course: ')
            perc = float(input('Enter Percentage: '))
            add_grades([course, roll_no, perc])
        elif user == 10:
            add_from_file()
        elif user == 11:
            roll_no = input('Enter Roll No: ')
            view_grade_sw(req_roll_no=roll_no)
        elif user == 12:
            roll_no = input('Enter Roll No: ')
            course = input('Enter Course: ')
            perc = float(input('Enter new percentage: '))
            edit_grade(req_roll_no=roll_no, req_course=course, new_marks=perc)
        elif user == 13:
            roll_no = input('Enter Roll No: ')
            course = input('Enter Course: ')
            delete_grade(req_roll_no=roll_no, req_course=course)
        elif user == 14:
            roll_no = input('Enter Roll No: ')
            view_grade_sw(req_roll_no=roll_no)
        elif user == 15:
            course = input('Enter the course: ')
            view_grade_cw(req_course=course)
        elif user == 16:
            award_list()
        elif user == 17:
            summary_sheet()
        elif user == 18:
            print('Enter the range of roll no:')
            start = int(input('From: '))
            end = int(input('To: '))
            transcript(start, end)
        user = int(input('Enter 1 to exit, 2 to continue: '))
    print('Exiting the system!')
main()
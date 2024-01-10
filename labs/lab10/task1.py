def menu():
    user_input = input('a) add, s) search, d) delete, l) list all, e) edit, q) quit: ')
    if user_input == 'a':
        add_course()
        print('Course Added')
    elif user_input == 's':
        searched = input('Enter Course code you want to search: ')
        search(searched)
    elif user_input == 'd':
        delete = input('Enter Course code you want to delete: ')
        delete_course(delete)
    elif user_input == 'l':
        list_all()
    elif user_input == 'e':
        code = input('Enter Course code you want to edit: ')
        new_hours = input('Enter credit hours you want to change: ')
        edit(code, new_hours)
    elif user_input == 'q':
        print('Quitted')
    else:
        print('InValid Input.')
def add_course():
    with open('crsfile.txt', 'a') as course_file:
        code = 'ISL'
        title = 'Intro to Information and Communication Technology'
        credit_hours = 3
        sem = 3
        type = 'core'
        content = f'{code}\t{title}\t{credit_hours}\t{sem}\t{type}\n'
        course_file.write(content)
    course_file.close()
# add_course()

def delete_course(code):
    new_lines = []
    with open('crsfile.txt', 'r') as course_file:
        lines = course_file.readlines()
        for line in lines:
            splitted_line = line.split()
            crs_code = splitted_line[0]
            if code != crs_code:
                new_lines.append(line)
    
    with open('crsfile.txt', 'w') as writefile:
        for line in new_lines:
            writefile.write(line)
# def delete_course(code):
#     new_lines = []
#     with open('crsfile.txt', 'r') as file:
#         lines = file.readlines()
#         for line in lines:
#             crs_code = line.split()[0]
#             crs_code = crs_code.strip()
#             if crs_code != code:
#                 new_lines.append(line)
#                 print(line)
#     with open('crsfile.txt', 'w') as file:
#         for line in new_lines:
#             file.write(line)


delete_course('ISL')

def search(code):
    with open('crsfile.txt', 'r') as course_file:
        lines = course_file.readlines()
        for line in lines:
            splitted_line = line.split()
            crs_code = splitted_line[0]
            if code == crs_code:
                print(str(line))
                break
# search('IICT')

def list_all():
    with open('crsfile.txt', 'r') as course_file:
        lines = course_file.readlines()
        for line in lines:
            print(line)
# list_all()

def edit(code, new_crhrs):
    new_lines = []
    with open('crsfile.txt', 'r') as course_file:
        lines = course_file.readlines()
        for line in lines:
            splitted_line = line.split()
            crs_code = splitted_line[0]
            if code == crs_code:
                crs_title = splitted_line[1] +  ' ' + splitted_line[2] + ' ' +  splitted_line[3] +  ' ' + splitted_line[4] +  ' ' + splitted_line[5] +  ' ' + splitted_line[6]
                crs_hrs = new_crhrs
                crs_type = splitted_line[8]
                content = f'{crs_code} {crs_title} {crs_hrs} {crs_type}'
                new_lines.append(content)
            else:
                new_lines.append(line)
    with open('crsfile.txt', 'w') as writefile:
        for line in new_lines:
            writefile.write(line)
# edit('ALP',5)
# menu()
# 
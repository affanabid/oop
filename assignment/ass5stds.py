import struct

format_string_stdtnts = '11s30s2sif11s'

# Funtion to check if a student is already present  
def valid_studenet(data):
    with open('students_data.bin','rb') as binary_file:
         roll_nmbr=data[0]
         while True:
           packed_data=binary_file.read(struct.calcsize('11s30s2sif11s1s'))
           if not packed_data:
             break

           unpacked_data=struct.unpack('11s30s2sif11s1s',packed_data)
           if unpacked_data[0].decode('utf-8')==roll_nmbr:
               return True
    return False

# Function to add a student to the binary file

def add_student(data):
    roll_no=data[0].encode('utf-8')
    name=data[1].encode('utf-8')
    dept_code=data[2].encode('utf-8')
    sem=data[3]
    percent=data[4]
    phone=data[5].encode('utf-8')

    if valid_studenet(data):
      raise ValueError('Student already present')
    else:
      byte=struct.pack(format_string_stdtnts,roll_no,name,dept_code,sem,percent,phone)
      with open('students_data.bin','ab') as binary_file:
        binary_file.write(byte)
        binary_file.write(b'\n')

# Funtion to view a student by his Roll-Number
def view_stdnt(roll_no):
    with open('students_data.bin','rb') as binary_file:
        
        while True:
            packed_data=binary_file.read(struct.calcsize('11s30s2sif11s1s'))
            if not packed_data:
                break

            unpacked_data=struct.unpack('11s30s2sif11s1s',packed_data)
            if unpacked_data[0].decode('utf-8')==roll_no:
                roll_no=unpacked_data[0].decode('utf-8')
                name=unpacked_data[1].decode('utf-8')
                dept_code=unpacked_data[2].decode('utf-8')
                sem=unpacked_data[3]
                percent=unpacked_data[4]
                phone=unpacked_data[5].decode('utf-8')

                print(f'Roll-no: {roll_no}\nName: {name}\nDepartment Code:{dept_code}\nSemester:{sem}\nPercentage:{int(percent)}\nPhone-no:{phone}')
                break

def delete_stdnt(roll_no):
    with open('students_data.bin','rb') as binary_file:
        student_list=[]
        while True:
          packed_data=binary_file.read(struct.calcsize(format_string_stdtnts))
          if not packed_data:
             break
          
          unpacked_data=struct.unpack(format_string_stdtnts,packed_data)
          if unpacked_data[0].decode('utf-8')!=roll_no:
             student_list.append(unpacked_data)

    with open('students_data.bin','wb') as binary_file:
       for student in student_list:
          packed_data=struct.pack(format_string_stdtnts,student)
          binary_file.write(packed_data)
          binary_file.write('\n')
    
# add_student(['BSDSF19A039','Jakib Hussein','DS',7,99.4,'090708601'])
# add_student(['BSDSF22A018','Emran Kaleeem','DS',2,87.3,'009977112'])
# view_stdnt('BSDSF19A019')
# delete_stdnt('BSDSF19A017')
import struct

student_struct = struct.Struct('11s30s2si11sf11s')  # Define your structure based on data types and lengths

def add_student(file, data):
    # Padding the name and phone number to fit the specified lengths
    padded_name = data[1].ljust(30)[:30]
    padded_phone = data[4].ljust(11)[:11]
    
    packed_data = student_struct.pack(
        data[0].encode('utf-8'),
        padded_name.encode('utf-8'),
        data[2].encode('utf-8'),
        data[3],
        padded_phone.encode('utf-8'),
        data[5],
        data[6].encode('utf-8')
    )
    file.write(packed_data)

def view_student(file, roll_no):
    file.seek(0)  # Reset file pointer
    while True:
        packed_data = file.read(student_struct.size)
        if not packed_data:
            break
        unpacked_data = student_struct.unpack(packed_data)
        if unpacked_data[0].decode('utf-8').strip() == roll_no:
            return list(item.decode('utf-8') if isinstance(item, bytes) else item for item in unpacked_data)

with open('students.bin', 'ab+') as file:
    add_student(file, (
        '12345678901',
        'John Doe',
        'CS',
        1,
        '00000000000',
        85.5,
        '12345678901'
    ))
    student_data = view_student(file, '12345678901')
    print(student_data)

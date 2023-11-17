
def valid_roll_no(line):
    for i in range(10):
        if line[i] == ' ':
            return False
        
def valid_name(line):
    for i in range(10, 42):
        if line[i] == '1' or line[i] == '2' or line[i] == '3' or line[i] == '4' or line[i] == '5' or line[i] == '6' or \
        line[i] == '7' or line[i] == '8' or line[i] == '9' or line[i] == '0':
            return False
        
def valid_course(line):
    i = 42
    if line[i] == ' ' and line[i+1] == ' ' and line[i+2] == ' ' and line[i+3] == ' ' and line[i+4] == ' ' and line[i+5] == ' ' and line[i+6] == ' ':
            return False
    
def valid_md(line):
    a = 49
    b = 50
    if ord(line[a]) < 48 and ord(line[a]) > 57:
        return False
    if ord(line[b]) < 48 and ord(line[b]) > 57:
        return False

def read_write(input_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        infile.readline()
        infile.readline()
        for i in range(21):
            line = infile.readline()
            if valid_roll_no(line) == False:
                outfile.write(f'record {i}: ')
                outfile.write(line)
            if valid_name(line) == False:
               outfile.write(f'record {i}: ')
               outfile.write(line)
            if valid_course(line) == False:
                outfile.write(f'record {i}: ')
                outfile.write(line)
            # if valid_md(line) == False:
            #     outfile.write(line)
            
        outfile.close()

if __name__ == "__main__":
    input_file = "grades.txt"
    output_file = "newfile"

    valid = read_write(input_file)

# def is_number(value):
#     try:
#         float(value)
#         return True
#     except ValueError:
#         return False



# def process_file(input_file, output_file):
    # with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
#         errors_count = 0
#         line_number = 1

#         for line in infile:
#             # Skip the first two lines (headers)
#             if line_number <= 2:
#                 line_number += 1
#                 continue

#             # Split the line into fields
#             record = line.strip().split()

#             # Validate the record
#             if validate_record(record):
#                 # Write line number and record to the output file
#                 outfile.write(f"{line_number}\n{' '.join(record)}\n")
#                 errors_count += 1

#             line_number += 1

#         return errors_count


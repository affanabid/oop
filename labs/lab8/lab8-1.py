with open("grades.txt") as file1:
    with open("errors.txt", "w") as file2:

        line = file1.readline()
        file2.writelines(line)
        line = file1.readline()
        file2.writelines(line)

        errors = 0
        lineno = 3
        line = file1.readline()
        while line != "":
            rollno = line[0:10]
            name = line[10:41]
            sess = line[52:54]
            if len(line) != 58:
                errors += 1
                file2.writelines(str(lineno)+"\n")
                file2.writelines(line)   
            elif len(rollno.strip()) != 10:
                    errors += 1
                    file2.writelines(str(lineno)+"\n")
                    file2.writelines(line)
            elif not (sess[0] >= '0' and sess[0] <= '9' and sess[1] >= '0' and sess[1] <= '9'):
                    errors += 1
                    file2.writelines(str(lineno)+"\n")
                    file2.writelines(line)
            lineno += 1
            line = file1.readline()

if errors == 0:
    print("grades file is error FREE")
else:
    print(errors, "errors are present in grades file")
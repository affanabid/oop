with open("grades.txt") as file1:
    with open("errors.txt", "w") as file2:

        s = file1.readline()   # read and skip first header line
        file2.writelines(s)
        s = file1.readline()   # read and skip second header line
        file2.writelines(s)

        errs = 0
        lineno = 3
        s = file1.readline()   # read first record line
        while s != "":
            rollno = s[0:10]
            name = s[10:41]
            sess = s[52:54]
            if len(s) != 58:
                errs += 1
                file2.writelines(str(lineno)+"\n")
                file2.writelines(s)   
            elif len(rollno.strip()) != 10:
                    errs += 1
                    file2.writelines(str(lineno)+"\n")
                    file2.writelines(s)
            elif not (sess[0] >= '0' and sess[0] <= '9' and sess[1] >= '0' and sess[1] <= '9'):
                    errs += 1
                    file2.writelines(str(lineno)+"\n")
                    file2.writelines(s)
            lineno += 1
            s = file1.readline()   # read next record line
            
if errs == 0:
    print("grades file is error FREE")
else:
    print(errs, "errors are present in grades file")
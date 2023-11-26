with open("errors.txt") as file1:
    with open("grades.txt", "r+") as file2:
        file1.readline()
        file1.readline()
        
        line = file1.readline()
        while line != "":
            lineno = int(line)
            line = file1.readline()
            file2.seek((lineno-1)*59)
            file2.writelines(line)
            line = file1.readline()

print("Update done")

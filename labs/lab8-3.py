students_data = {}

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

with open('grade.txt', 'r') as file:
    for line in file:
        parts = line.split()
        student_id = parts[0]
        course_data = {
            "name": parts[1] + '\t' + parts[2],
            "Crs": parts[3],
            "Md": parts[4],
            "Ss": parts[5],
            "Fn": parts[6],
            "total": int(parts[4]) + int(parts[5]) + int(parts[6]),
        }

        if student_id in students_data:
            students_data[student_id].append(course_data)
        else:
            students_data[student_id] = [course_data]

print('\t\t\t\t\t    University of the Punjab')
print('\t\t\t\t\tCollege of Information Technology')
print('\t\t\t\t\t  Result Session : Spring 2010')
print('Degree: BIT')
print('Sr. No. Roll No\t\tStudent Name\t\t\tITC\tPF\tDLD\tTOTAL\t%age\tGrade')
print('======================================================================================================')
it_students = 0
it_itc_total = 0
it_pf_total = 0
it_dld_total = 0
it_all_total = 0
for student_id in students_data:
    student = students_data[student_id]
    itc = student[0]
    pf = student[1]
    dld = student[2]
    total_marks = itc['total'] + pf['total'] + dld['total']
    percentage = round(total_marks / 300 * 100, 1)
    grade = assign_grade(percentage)
    if student_id[1] == 'I' and student_id[2] == 'T':
        it_students += 1
        print(f"{it_students}\t{student_id}\t{itc['name']}\t\t\t{itc['total']}\t{pf['total']}\t{dld['total']}\t{total_marks}\t{percentage}% \t{grade}")
        it_itc_total += itc['total']
        it_pf_total += pf['total']
        it_dld_total += dld['total']
        it_all_total += total_marks
it_itc_average = int(it_itc_total / it_students)
it_pf_average = int(it_pf_total / it_students)
it_dld_average = int(it_dld_total / it_students)
it_total_average = it_all_total // it_students
print(f'\t\t\t\t======================================================================')
print(f'\t\t\t\tBIT degree average: \t{it_itc_average}\t{it_pf_average}\t{it_dld_average}\t{it_total_average}')
print()

print('Degree: BSE')
print('Sr. No. Roll No\t\tStudent Name\t\t\tITC\tPF\tDLD\tTOTAL\t%age\tGrade')
print('=====================================================================================================')
se_students = 0
se_itc_total = 0
se_pf_total = 0
se_dld_total = 0
se_all_total = 0
for student_id in students_data:
    student = students_data[student_id]
    itc = student[0]
    pf = student[1]
    dld = student[2]
    total_marks = itc['total'] + pf['total'] + dld['total']
    percentage = round(total_marks / 300 * 100, 1)
    grade = assign_grade(percentage)
    if student_id[1] == 'S' and student_id[2] == 'E':
        se_students += 1
        print(f"{se_students}\t{student_id}\t{itc['name']}\t\t\t{itc['total']}\t{pf['total']}\t{dld['total']}\t{total_marks}\t{percentage}% \t{grade}")
        se_itc_total += itc['total']
        se_pf_total += pf['total']
        se_dld_total += dld['total']
        se_all_total += total_marks
se_itc_average = int(se_itc_total / se_students)
se_pf_average = int(se_pf_total / se_students)
se_dld_average = int(se_dld_total / se_students)
se_total_average = se_all_total // se_students
print(f'\t\t\t\t======================================================================')
print(f'\t\t\t\tBSE degree average: \t{se_itc_average}\t{se_pf_average}\t{se_dld_average}\t{se_total_average}')
print()
overall_itc_average = (it_itc_total + se_itc_total) // (it_students + se_students)
overall_pf_average = (it_pf_total + se_pf_total) // (it_students + se_students)
overall_dld_average = (it_dld_total + se_dld_total) // (it_students + se_students)
overall_total_average = (it_all_total + se_all_total) // (it_students + se_students)
print(f'\t\t\t\t======================================================================')
print(f'\t\t\t\tOverall    average: \t{overall_itc_average}\t{overall_pf_average}\t{overall_dld_average}\t{overall_total_average}')
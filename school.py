import sys

supervisor_list = []
supervisor_dict = {}

teacher_list = []
teacher_dict = {}

student_list = []
student_dict = {}

position = ["supervisor", "teacher", "student", "end"]

while True:
    lines = input()
    # print(lines)
    if lines in position:
        if lines == "supervisor":
            supervisor_dict["User"] = lines
            lines = input()
            supervisor_dict["Name"] = lines
            lines = input()
            supervisor_dict["School_classes"] = lines
            print("")
            supervisor_list.append(supervisor_dict)
            print(f'{supervisor_dict["User"]}\n{supervisor_dict["Name"]}\n{supervisor_dict["School_classes"]}')
        if lines == "teacher":
            teacher_dict["User"] = lines
            lines = input()
            teacher_dict["Name"] = lines
            lines = input()
            teacher_dict["Subject"] = lines
            lines = input()
            teacher_dict["School_class"] = lines
            print("")
            teacher_list.append(teacher_dict)
            print(f'{teacher_dict["User"]}\n{teacher_dict["Name"]}\n{teacher_dict["Subject"]}\n{teacher_dict["School_class"]}')
        if lines == "student":
            student_dict["User"] = lines
            lines = input()
            student_dict["Name"] = lines
            lines = input()
            student_dict["School_classes"] = lines
            student_list.append(student_dict)
            print(f'{student_dict["User"]}\n{student_dict["Name"]}\n{student_dict["School_classes"]}')
        if lines == "end":
            print("end")
    else:
        continue

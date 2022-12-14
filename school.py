import sys

supervisor_list = []
supervisor_dict = {}
supervisors_dict = {}

teacher_list = []
teacher_dict = {}
teachers_dict = {}

student_list = []
student_dict = {}
students_dict = {}

school_dict = {}

one_class_dict = {
    "Class_name": None,
    "Teachers": [],
    "Supervisor": None,
    "Students": [],
}

position = ["supervisor", "teacher", "student", "end"]

while len(sys.argv) > 1:
    lines = input()
    # print(lines)
    if lines in position:
        if lines == "supervisor":
            supervisor_dict = {}
            supervisor_dict["User"] = lines
            lines = input()
            supervisor_dict["Name"] = lines
            supervisor_dict["School_classes"] = []
            while True:
                lines = input()
                if not lines:
                    break
                supervisor_dict["School_classes"].append(lines)
                if lines not in school_dict:
                    school_dict[lines] = {
                        "Class_name": None,
                        "Teachers": [],
                        "Supervisor": None,
                        "Students": [],
                    }
                school_dict[lines]["Supervisor"] = supervisor_dict
            supervisor_list.append(supervisor_dict.copy())
            supervisors_dict[supervisor_dict["Name"]] = supervisor_dict
            print(f'{supervisor_dict["User"]}\n{supervisor_dict["Name"]}')
            print(*supervisor_dict["School_classes"], sep="\n")
            print("")
        if lines == "teacher":
            teacher_dict = {}
            teacher_dict["User"] = lines
            lines = input()
            teacher_dict["Name"] = lines
            lines = input()
            teacher_dict["Subject"] = lines
            teacher_dict["School_class"] = []
            while True:
                lines = input()
                if not lines:
                    break
                teacher_dict["School_class"].append(lines)
                if lines not in school_dict:
                    school_dict[lines] = {
                        "Class_name": None,
                        "Teachers": [],
                        "Supervisor": None,
                        "Students": [],
                    }
                school_dict[lines]["Teachers"].append(teacher_dict)
            teacher_list.append(teacher_dict.copy())
            teachers_dict[teacher_dict["Name"]] = teacher_dict
            print(f'{teacher_dict["User"]}\n{teacher_dict["Name"]}\n{teacher_dict["Subject"]}')
            print(*teacher_dict["School_class"], sep="\n")
            print("")
        if lines == "student":
            student_dict = {}
            student_dict["User"] = lines
            lines = input()
            student_dict["Name"] = lines
            lines = input()
            if not lines in school_dict:
                school_dict[lines] = {
                    "Class_name": None,
                    "Teachers": [],
                    "Supervisor": None,
                    "Students": [],
                }
            student_dict["School_classes"] = lines
            school_dict[lines]["Students"].append(student_dict.copy())
            student_list.append(student_dict.copy())
            students_dict[student_dict["Name"]] = student_dict
            print(f'{student_dict["User"]}\n{student_dict["Name"]}\n{student_dict["School_classes"]}')
        if lines == "end":
            print("end")
            break
    else:
        continue

terminal_input = sys.argv[1]
if len(terminal_input) == 2:
    print(f'\n******** PHASE QUERY ********\n')
    print("Supervisor: ", school_dict[terminal_input]["Supervisor"])
    print("Students: ", *school_dict[terminal_input]["Students"], sep="\n")
if terminal_input in supervisors_dict:
    print(f'\n******** PHASE QUERY ********\n')
    print("Supervisor: ", supervisors_dict[terminal_input])
    for classes in supervisors_dict[terminal_input]["School_classes"]:
        print("Students: ", *school_dict[classes]["Students"], sep="\n")

if terminal_input in teachers_dict:
    print(f'\n******** PHASE QUERY ********\n')
    for mutual_classes in teachers_dict[terminal_input]["School_class"]:
        print(school_dict[mutual_classes]["Supervisor"])

if terminal_input in students_dict:
    print(f'\n******** PHASE ********\n')
    student_one_class = students_dict[terminal_input]["School_classes"]
    print(*school_dict[student_one_class]['Teachers'], sep="\n")





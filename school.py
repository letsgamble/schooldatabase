supervisor_list = []
supervisor_dict = {}
# mentor = {"Name": name, "Subject": subject, "Class": school_class}
# student = {"Name": name, "Class": school_class}


def user_type():
    check_who = input()
    if check_who == "supervisor":
        name = input()
        supervisor_dict["User"] = check_who
        supervisor_dict["Name"] = name
        supervisor_list.append(supervisor_dict)
        check_class = input()
        while check_class != "":
            supervisor_dict["School_class"] = check_class
            supervisor_list.append(supervisor_dict)
            input()

    if check_who == "mentor":
        print("To jest mentor")
    if check_who == "student":
        print("To jest student")
    if check_who == "end":
        print("To jest student")


user_type()
print("List:", supervisor_list)

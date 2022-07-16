school_class = str()
subject = str()

rows = [
    ("supervisor", {"Class": school_class}),
    ("mentor", {"Subject": subject, "Class": school_class}),
    ("student", {"Class": school_class}, )
]


def user_type():
    checkwho = input()
    if checkwho == "supervisor":
        print("To jest supervisor")
    if checkwho == "mentor":
        print("To jest mentor")
    if checkwho == "student":
        print("To jest student")
    if checkwho == "end":
        print("To jest student")


user_type()

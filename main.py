# Header
# Paul Schutte
# Dean's List Checker
# This App takes a students inputs and lets them know if they have made the dean's list or the honor roll
while True:

    l_name = input("Enter your last name (ZZZ to quit)")
    if l_name == 'ZZZ':
        break
    lastname = str(l_name)
    f_name = input("Enter your first name")
    firstname = str(f_name)
    grades = input("Enter your GPA a a decimal number")
    GPA = float(grades)
    if GPA > 3.5:
        print(lastname, firstname, "you have made the Dean's List!")
    elif GPA > 3.25:
        print(lastname, firstname, "you have made the Honor Roll!")

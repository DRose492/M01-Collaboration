# Alex Sampson
# GPA Checker
# Checks to see if a given student's name and GPA qualifies for specified marks/ranks

# Detailing the variables needed
first_name = ""
last_name = ""
grade = 0

# Writing the code
first_name = input("What is the first name of the student? ")
last_name = input("What is the last name of the student? ")
grade = float(input("What is this student's GPA? "))

while last_name != "ZZZ":
    if grade > 3.49:
        print(first_name + last_name + "'s GPA would make them the Dean's List!!!")
    elif grade > 3.24 and grade < 3.5:
        print(first_name + last_name + "'s GPA has made the Honor Roll")
    else:
        print(first_name + last_name + "'s GPA didn't make either the Honor Roll or the Dean's List")
    print()
    first_name = input("Please the next student's first name. ")   
    last_name = input("Please the next student's last name. If there is no more students to enter, enter ZZZ ")
    grade = float(input("Enter the next student's GPA "))

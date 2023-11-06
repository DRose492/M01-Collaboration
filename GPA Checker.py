# Alex Sampson
# GPA Checker
# Checks to see if a given student's name and GPA qualifies for specified marks/ranks

# Detailing the variables needed
name = ""
grade = 0

# Writing the code
name = input("What is the name of the student? ")
grade = float(input("What is this student's GPA? "))

while name != "ZZZ":
    if grade > 3.49:
        print(name + "'s GPA would make them the Dean's List!!!")
    elif grade > 3.24 and grade < 3.5:
        print(name + "'s GPA has made the Honor Roll")
    else:
        print(name + "'s GPA didn't make either the Honor Roll or the Dean's List")
    print()    
    name = input("Please enter the next student. If there is no more students to enter, enter ZZZ ")
    grade = float(input("Enter the next student's GPA "))
from Student import Student

studentOne = Student("Marco","Accounting", 3.4, False)
studentTwo = Student("Cristina", "Sales", 3.6, False)
studentTre = Student("Mayra", "Purchase", 3.5, True)
studentFor = Student("Mariana", "Sales", 2.8, True)
studentFiv = Student("Carlos", "Accounting", 3.3, False)

students = [studentOne, studentTwo, studentTre, studentFor, studentFiv]

print("List length: " + str(len(students)) + " students")

print("\n********** INFORMATION LOADED **********\n")

for stu in students:
    print(stu.name + " the result is: " + str(stu.on_honor_roll()) + " your gpa is: " + str(stu.gpa) + " and your time: " + str(stu.year_category_student()) + ".")

print("\n********** INFORMATION FINISHED **********")
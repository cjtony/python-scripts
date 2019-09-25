import sys as sistem
from Student import Student

print("Hello! write your name for continue...")

nameEnv = input()
counter = 0
flagStr = False

while nameEnv == "":
    counter += 1
    print("Write your name is obligatory!")
    nameEnv = input()
    if counter == 3:
        print("You have reached 4 failed attempts. Finished program.")
        sistem.exit()

def loadInformation(nameEnv):
    nameEnv = str(str.capitalize(nameEnv))
    student1 = Student(nameEnv, 'Business', 3.1, False)
    name = student1.name
    major = student1.major
    gpa = student1.gpa
    iop = student1.is_on_probation
    print("\n*********** Information Loaded... ***********\n")
    print("Hello " + name + "!, your major is " + major + ", your gpa is " + str(gpa) + " and finally is on aprobation: " + str(iop)  )

loadInformation(nameEnv)

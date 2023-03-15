studentList = ["Berkan Bilgin","Utku Gül"]

def addStudent(name):
    studentList.append(name)

def removeStudent(name):
    studentList.remove(name)

def addStudents():
    number = int(input("How many students do you want to add?"))

    for x in range(number) :
        name = input("Student name:")
        addStudent(name)

def printStudents():
    n = 0
    while n < len(studentList):
        print(n+1,studentList[n])
        n += 1


def findStudentNumber():
    name = input("Enter the student name for which you want to find the student number:")
    print(studentList.index(name) + 1)

def removeStudents():
    number = int(input("How many students do you want to remove?"))

    for x in range(number) :
        name = input("Enter Student Name:")
        removeStudent(name)



addStudent("Mehmet Ata")
removeStudent("Utku Gül")
addStudents()
findStudentNumber()
removeStudents()
printStudents()

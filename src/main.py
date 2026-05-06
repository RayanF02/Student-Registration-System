courses = {}
students = {}


class StudentExistsError(Exception):
    pass


class StudentNotExistsError(Exception):
    pass


def startwork():
    global courses
    global students
    courses_file = open('courses.txt')
    line = courses_file.readline()
    while line:
        x = line.split()
        courseid = x[0]
        tit = x[1]
        prereq = x[2:]
        courses[courseid] = {
            'title': tit,
            'pq': prereq
        }
        line = courses_file.readline()
    courses_file.close()
    students_file = open('students.txt')
    line = students_file.readline()
    while line:
        x = line.split()
        studid = x[0]
        name = x[1]
        taken = x[2:]
        students[studid] = {
            'name': name,
            'taken': taken
        }
        line = students_file.readline()
    students_file.close()

def endwork():
    lst_students = []
    for id in students:
        student_string = id + ' ' + students[id]["name"]
        for course in students[id]['taken']:
            student_string = student_string + ' ' + course
        student_string = student_string + '\n'
        lst_students.append(student_string)
    lst_students[-1] = lst_students[-1][:-1]
    file = open("students.txt", 'w')
    file.writelines(lst_students)
    file.close()

def newcourse(courseid, studid):
    global students
    for i in courses[courseid]["pq"]:
        if i in students[studid]["taken"]:
            continue
        else:
            print('Prerequisites not met')
            return
    else:
        students[studid]["taken"].append(courseid)
        print('Added successfully')

def newstudent(id, name, courses_taken):
    global students
    if id in students:
        raise StudentExistsError
    else:
        students[id] = {
            'name': name,
            "taken": courses_taken
        }
        print('Added successfully')

def removestudent(id):
    if not (id in students):
        raise StudentNotExistsError
    else:
        del students[id]
        print('Removed successfully')

def coursesleft(id):
    num = 0
    for course in courses:
        if not (course in students[id]["taken"]):
            num += 1
    return num

def coursesrepeated(id):
    unrepeated = []
    repeated = []
    for course in students[id]["taken"]:
        if course in unrepeated:
            if not (course in repeated):
                repeated.append(course)
        unrepeated.append(course)
    if len(repeated) == 0:
        repeated = ['No repeated courses']
    return repeated

try:
    startwork()
    stop = False
    print('STUDENT REGISTRATION SYSTEM')
    print('Enter 1 to show students taken courses')
    print('Enter 2 to register new course')
    print('Enter 3 to register a new student')
    print('Enter 4 to remove a student from database')
    print('Enter 5 to show how many courses left until graduation')
    print('Enter 6 to show students repeated courses')
    print('\nEnter 0 to exit with saving')
    print('Enter -1 to exit without saving')
    while not stop:
        choose = str(input('Enter your choice: '))
        if choose not in ('1', '2', '3', '4', '5', '6', '0', '-1'):
            print("Error, not valid choice")
        elif choose == '1':
            id = input('Enter student ID: ')
            for i in students[id]['taken']:
                print(i, end=' ')
            print()
        elif choose == '2':
            id = input('Enter student ID: ')
            course = input('Enter course ID: ')
            if not (course in courses):
                print('Invalid course')
                continue
            if not (id in students):
                raise StudentNotExistsError
            newcourse(course, id)
        elif choose == '3':
            id = input('Enter student ID: ')
            name = input("Enter name using underscores: ")
            courses_taken = input('Enter courses separated by spaces: ').split()
            newstudent(id, name, courses_taken)
        elif choose == '4':
            id = input('Enter student ID to remove: ')
            removestudent(id)
        elif choose == '5':
            id = input('Enter student ID: ')
            x = coursesleft(id)
            print(x, 'courses left until graduation')
        elif choose == '6':
            id = input('Enter student ID: ')
            x = coursesrepeated(id)
            for i in x:
                print(i, end=' ')
            print()
        elif choose == '0':
            print('Goodbye')
            endwork()
            stop = True
        elif choose == '-1':
            print('Goodbye')
            stop = True
except KeyError:
    print('Invalid student/course ID, program stops running')

except StudentExistsError:
    print("Unable to add existing student. Program stops running")

except StudentNotExistsError:
    print("Unable to remove non-existing student. Program stops running")

except FileNotFoundError:
    print('Files students.txt and courses.txt are required for program. Unable to run')

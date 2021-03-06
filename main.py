import datetime  # we will use this for date objects
from person import Person
from student import Student
from lecturer import Lecturer
from course import Course

print('--- defining lecturers ----')
lecturer1 = Lecturer('Whoever', 'Ben-Zakkai', datetime.date(1979, 1, 3)
                     , 'Some addr', 19, frozenset(), 2020, 150)

lecturer2 = Lecturer('Whoever2', 'Ben-Shlomo', datetime.date(1990, 4, 17)
                     , 'Some addr2', 20, frozenset(), 2020, 150)


print('--- defining students ----')

student1 = Student("Muhammad", "Ben-Ami", datetime.date(1990, 1, 11)
                   , "Some street 13 at Some City", 15,
                   frozenset(),
                   2020)

student2 = Student("Iris", "York", datetime.date(1982, 4, 16)
                   , "Some street 14 at Some City", 16,
                   frozenset(), 2020)


# define courses, not attached to lecturers!
python = Course("Python", 120, datetime.time(10, 00, 00), "Wednesday", 0)
python.lecturer_id = lecturer1.id
sforce = Course("Salesforce", 90, datetime.time(16, 00, 00), "Wednesday", 0)
sforce.lecturer_id = lecturer2.id
javascr1 = Course("JavaScript", 120, datetime.time(11, 30, 00), "Tuesday", 0)
javascr1.lecturer_id = lecturer1.id
cshp = Course("C#", 120, datetime.time(16, 00, 00), "Tuesday", 0)
cshp.lecturer_id = lecturer2.id

# add courses to students
student1.courses = frozenset([python, javascr1, cshp])
student2.courses = frozenset([python, sforce])
student2.courses = frozenset([python, sforce, javascr1])


lecturer1.courses = frozenset([python, javascr1])
lecturer2.courses = frozenset([cshp, sforce])
print('--------')

# please define some of your courses

print('----student\'s courses ----')

print(student1.get_my_courses_as_str())  # returns courses with no sorting
print(student1.get_my_schedule()) # shall print lessons by weekdays and time,
print(student1.who_teaches_me(python))  # shall print Lecturer name and course name

print('----student\'s courses ----')
# student2.takes_courses()
print('----lecturer\'s courses ----')

print(lecturer1.i_teach_courses()) # shall print courses (name, from-to time, by weekdays)
print(lecturer2.who_takes_my_course_str(python)) # shall print all students names by course


ret = lecturer1.teaches_students(frozenset([student1, student2]))
print(ret)
print('--------')
ret = student1.name + ' \n' + student1.takes_courses_from(frozenset([lecturer1]))
print(ret)

print('--------')
print('-------- 3 --------')
person = Person("שירלי", "משולם", datetime.date(1992, 5, 2),  # year, month, day
                "רח' שבי בשקט 13",
                310156455)  # 12345678", "sh.meshulam@example.com")
print(person.name, ": ", person.age())
# print(person.email)
person.birth_date = datetime.date(1992, 5, 7)
print(person.name, ": ", person.age())




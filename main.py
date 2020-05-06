import datetime  # we will use this for date objects
from person import Person
from student import Student
from lecturer import Lecturer

student1 = Student("Muhammad", "Ben-Ami", datetime.date(1990, 1, 11)
                   , "Some street 13 at Some City", 15,
                   frozenset(['Python', 'Java']),
                   2020)
student2 = Student("Iris", "York", datetime.date(1982, 4, 16)
                   , "Some street 14 at Some City", 16,
                   frozenset(['Python', 'C#']), 2020)
# student2.name = 'Boris'
student2.surname = 'Sholkov'
# student1.name = student2.name
print(student2.birth_date.month)
print('--------')
lecturer1 = Lecturer('Whoever', 'Ben-Zakkai', datetime.date(1979, 1, 3)
                     , 'Some addr', 19,
                     frozenset(['Python', 'Advanced Algorithms']), 2020, 150)



student1.takes_courses()
print('--------')
student2.takes_courses()

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
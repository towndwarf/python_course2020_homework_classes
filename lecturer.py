import datetime
from person import Person
from student import Student
from datetime import date  # we will use this for date objects


class Lecturer(Person):
    def __init__(self, name: str, surname: str, birth_date: date, address: str
                 , person_id: int, courses: frozenset,
                 study_year: int) -> None:
        super().__init__(name, surname, birth_date, address, person_id, courses, study_year)

    def teaches(self, stud: Student):
        return self.__str__() + ' teaches ' + self.print_courses()

    def teaches_students(self, students: frozenset):
        d = self.cmp_own_courses_to_persons(students)
        courses_cnt = len(d)
        ret = f'Lecturer {self.__str__()}\n in year {self.study_year} teaches'
        if courses_cnt == 0:
            return ret + 'no courses.'
        else:
            ret = f'{ret}: '


        for course in d:
            ret += f"\n{str((list(d[course])))} to {course}"
        return ret




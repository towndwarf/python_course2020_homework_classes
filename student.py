from person import Person
from datetime import date  # we will use this for date objects


# import lecturer


class Student(Person):
    def __init__(self, name: str, surname: str, birth_date: date, address: str, person_id: int, courses: frozenset,
                 study_year: int) -> None:
        super().__init__(name, surname, birth_date, address, person_id, courses, study_year)

    def takes_courses(self):
        ret = ''
        for crs in self.courses:
            ret += crs + ', '
        print(f"{str(self)}\n Courses in year {self.study_year}: {ret.rstrip(', ')}\n")

    # returns dictionary - course: lecturer
    # lecturers - frozenset of Lecturer
    def takes_courses_from(self, lecturers: frozenset) -> str:
        d = self.cmp_own_courses_to_persons(lecturers)
        ret = 'Takes:'
        for i in d:
            ret += f'\n - {str(list(d[i]))} from {str(i.name)}'
        return ret


"""
        d = dict()
        for crs in self.courses:
            for lct in lecturers:
                lecturer_who_teaches_course = frozenset(crs) & lct.courses
                if lecturer_who_teaches_course != frozenset():
                    d[crs] = lecturer_who_teaches_course
        return d
"""

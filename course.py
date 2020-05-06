from lecturer import Lecturer


class Course:

    def __init__(self, name: str, lecturer: Lecturer, length: float, times: []):
        self.__students = []
        self.__name = name
        self.__lecturer = lecturer
        self.__lesson_length = length
        self.__times = times # not defined, usually days of week

    def __get_name(self):
        return self.__name

    def __set_name(self, name):
        self.__name = name

    a = property(__get_name, __set_name)

    def __get_lecturer(self):
        return self.__lecturer

    def __set_lecturer(self, lecturer):
        self.__lecturer = lecturer

    def add_participants(self, student):
        self.__students.append(student)

    def remove_participants(self, student):
        self.__students.remove(student)

    def get_participants(self):
        return self.__students

    def __get_lesson_length(self):
        return self.__lesson_length

    def __set_lesson_length(self, length: float):
        self.__lesson_length = length


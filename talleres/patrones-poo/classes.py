from functools import reduce
from typing import Dict

MATH = "math"
BIOLOGY = "biology"
SPANISH = "spanish"


class Person:
    """
    Person Class
    """

    def __init__(self, name, last_name, birthday, id):
        self.name = name
        self.last_name = last_name
        self.birthday = birthday
        self.id = id


class Student(Person):
    """
    Class Student inherites from Person class to calculate 
    average course grades to Math, Biology and Spanish
    """

    __MAX_GRADES = 3
    __COUNT_ID = 1

    def __init__(self, name, last_name, birthday, id):
        super().__init__(name, last_name, birthday, id)
        self.biology = list()
        self.spanish = list()
        self.math = list()

    def __str__(self) -> str:
        return f"""
        Estudiante: {self.name} {self.last_name}
        id: {self.id}
        date: {self.to_dash_date(self.birthday)}
        Biología: {self.biology}
        Español: {self.spanish}
        Matemáticas: {self.math}
        """

    @classmethod
    def from_dict(cls, obj):
        cls.__COUNT_ID += 1
        return cls(obj["name"], obj["last_name"], obj["birthday"], cls.__COUNT_ID)

    def add_grade(self, grade: float, course: str) -> None:
        course = getattr(self, course)
        if len(course) < self.__MAX_GRADES:
            course.append(grade)
        else:
            raise Exception("Máximo número de notas agregadas")

    @staticmethod
    def to_dash_date(date: str) -> str:
        return date.replace("/", "-")

    @staticmethod
    def calc_avg(course: list) -> float:
        return reduce(lambda a, b: a + b, course) / len(course)

    def get_mean(self, course: str) -> str:
        avg = self.calc_avg(getattr(self, course))
        return f""" promedio {course} = {avg} """

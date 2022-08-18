from functools import reduce

MATH = "math"
BIOLOGY = "biology"
SPANISH = "spanish"


class Person:
    """
    Class Person 
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

    def __init__(self, name, last_name, birthday, id):
        super().__init__(name, last_name, birthday, id)
        self.biology = list()
        self.spanish = list()
        self.math = list()

    def __str__(self) -> str:
        return f"""
        Estudiante: {self.name} {self.last_name}
        Biología: {self.biology}
        Matemáticas: {self.math}
        Español: {self.spanish}
        """

    def add_grade(self, grade: float, course: str) -> None:
        course = getattr(self, course)
        if len(course) < self.__MAX_GRADES:
            course.append(grade)
        else:
            raise Exception("Máximo número de notas agregadas")

    def calc_avg(self, course: list) -> float:
        return reduce(lambda a, b: a + b, course) / len(course)

    def get_mean(self, course: str) -> str:
        avg = self.calc_avg(getattr(self, course))
        return f""" promedio {course} = {avg} """

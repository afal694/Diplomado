from classes import *


maria = Student("María", "Hernández", "15/04/1994", 1)


maria.add_grade(2.6, MATH)
maria.add_grade(3.5, MATH)
maria.add_grade(4.8, MATH)

maria.add_grade(4.3, BIOLOGY)
maria.add_grade(3.8, BIOLOGY)
maria.add_grade(3.5, BIOLOGY)

maria.add_grade(2.6, SPANISH)
maria.add_grade(3.4, SPANISH)
maria.add_grade(4.2, SPANISH)

print(maria)
print(maria.get_mean(MATH))
print(maria.get_mean(SPANISH))
print(maria.get_mean(BIOLOGY))

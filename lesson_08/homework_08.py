# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об'єкт цього класу, представляючи студента.
# Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
# Виведіть інформацію про студента та змініть його середній бал.

class Student:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.surname = kwargs.get('surname')
        self.age = kwargs.get('age')
        self.average_grade = kwargs.get('average_grade')

    def change_grade(self, grade=None):
        self.average_grade = grade
        print(f"Середній бал для {self.name} змінено на {grade}")

student_first = Student(name='Olha', surname='Perez', age=21, average_grade=12)
print(f"Студент: {student_first.name} {student_first.surname}, Вік: {student_first.age}, Бал: {student_first.average_grade}")
student_first.change_grade(10)



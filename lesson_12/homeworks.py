# First function
def string_filters(lst):
    return [char for char in lst if type(char) == str]

# Second function
class Student:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.surname = kwargs.get('surname')
        self.age = kwargs.get('age')
        self.average_grade = kwargs.get('average_grade')

    def change_grade(self, grade=None):
        if grade is None:
            self.average_grade = None
            return

        if not isinstance(grade, (int, float)):
            raise TypeError("Grade must be a number")

        if grade < 0:
            raise ValueError('Grade cannot be negative')

        self.average_grade = grade
        print(f"Середній бал для {self.name} змінено на {grade}")

# Third function
# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
def sum_even_numbers(num_list):
    new_list_even = [i for i in num_list if i % 2 == 0]
    return sum(new_list_even)

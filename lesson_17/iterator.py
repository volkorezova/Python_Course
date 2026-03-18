# Ітератори:
#
# Реалізуйте ітератор для зворотного виведення елементів списку.
# Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.

# list reverse iterator
class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration

        value = self.data[self.index]
        self.index -= 1
        return value

print("List reverse iterator")
for i in ReverseIterator( [1, 2, 3, 4, 5, 6, 7, 8]):
    print(i)

# even numbers iterator
class EvenNumIterator:
    def __init__(self, num):
        self.num = num
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.num:
            if self.current % 2 == 0:
                value = self.current
                self.current += 1
                return value
            self.current += 1

        raise StopIteration

print("Even number iterator")
for number in EvenNumIterator(10):
    print(number)
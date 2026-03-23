# Декоратори:
#
# Напишіть декоратор, який логує аргументи та результати викликаної функції.
# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.

# decorator logger
def logger_decorator(func):
    def wrapper(a, b):
        print("a =", a, "b =", b)
        result = func(a, b)
        print("result =", result)
        return result
    return wrapper

@logger_decorator
def add(a, b):
    return a + b

add(2, 3)

# exeption decorator
def exeption_decorator(func):
    def wrapper(a, b):
        try:
            return func(a, b)
        except:
            print("error")
    return wrapper

@exeption_decorator
def divide(a, b):
    print(a / b)

divide(10, 2)
divide(10, 0)
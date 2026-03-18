# Генератори:
#
# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.

# generator of even numbers
def even_numbers(n):
    i = 0
    while i <= n:
        if i % 2 == 0:
            yield i
        i += 1

print("Generator of even numbers")
for number in even_numbers(10):
    print(number)

# generator of Fibonachi
def fibonacci(n):
    a = 0
    b = 1

    while a <= n:
        yield a
        c = a + b
        a = b
        b = c

print("\nGenerator of Fibonachi")
for number in fibonacci(100):
    print(number)
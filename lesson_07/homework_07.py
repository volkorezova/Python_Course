# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        if  result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_numbers(first_number, second_number):
    return first_number + second_number
print(f'\nTask 2 - Sum of two numbers: {sum_numbers(3, 4)}')

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average_value(numbers):
    return sum(numbers) / len(numbers)
print(f'\nTask 3 - Average value: {average_value([1,3,4,6])}')

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(s):
    return s[::-1]
print(f'\nTask 4 - Reverse string: {reverse_string("REST")}')

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(word_list):
    longest = word_list[0]
    for word in word_list:
        if len(word) > len (longest):
            longest = word
    return longest
print(f'\nTask 5 - Longest word: {longest_word(["REST", 'reprogram', 'tetstststststsddd'])}')

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)

    for i in range(len_str1 - len_str2):
        if str1[i:i + len_str2] == str2:
            return i
    return -1

print('Task 6 - Find substring')

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
# task 7
"""Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()
"""

def unique_chars(string):
    unique = len(set(string))
    return unique > 10

print(unique_chars(input('\nTask 7 Enter your string: ')))

# task 8
"""
Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
(враховуються як великі так і маленькі).
Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".
"""
def words_required():
    word_req = input("Please enter your word: ")

    while 'h' not in word_req.lower():
        print("There is NO letter 'h'.")
        word_req = input("Please enter your word again: ")

    print("Thanks! Correct word was entered!")
    return word_req
result = words_required()

# task 9
"""Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
Напишіть код, який сформує новий list (наприклад lst2), який містить лише змінні типу стрінг,
які присутні в lst1. Данні в лісті можуть бути будь якими
"""
def string_selection(list_for_selection):
    lst2 = [char for char in list_for_selection if type(char) == str]
    return lst2

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
print(f'\nTask 9 Result of string selection: {string_selection(lst1)}')

# task 10
"""Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті"""
def sum_even_numbers(number_list):
    new_list_even = [i for i in number_list if i % 2 == 0]
    print(f'The list with even numbers: {new_list_even}')
    return sum(new_list_even)

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 4]
print(f'\nTask 10 - The total sum of even numbers: {sum_even_numbers(num_list)}')

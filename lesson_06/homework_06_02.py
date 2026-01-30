# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
# (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".
word = input("Please enter your word: ").lower()
while 'h' not in word:
    word = input("Please enter your word again: ").lower()
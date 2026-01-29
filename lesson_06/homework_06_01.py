# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

our_string = input()
print(set(our_string))
unique_chars = len(set(our_string))
if unique_chars > 10:
    print('True')
else:
    print('False')
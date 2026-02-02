# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 4]
new_list_even = [i for i in numbers_list if i % 2 == 0]
print(f'The list with even numbers: {new_list_even}')
total_sum = sum(new_list_even)
print(f'The total sum of even numbers: {total_sum}')


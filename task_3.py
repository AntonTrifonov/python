# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

my_list = [random.randint(1, 10) for i in range(10)]
print(my_list)
print(set(my_list))

new_list = []
for num in my_list:
    if num not in new_list:
        new_list.append(num)

print(new_list)

only_ones = []
for el in my_list:
    if my_list.count(el) == 1:
        only_ones.append(el)

print(only_ones)
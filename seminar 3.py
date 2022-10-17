# 1.Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import math

# my_list=[2, 3, 5, 9, 3]
#
# l = len(my_list)
# print("l = ", l)
#
# chet = []
# nechet = []
# for i in range(l):
#     if i % 2 == 0:
#         chet.append(my_list[i])
#     else:
#         nechet.append(my_list[i])
# print(sum(chet), sum(nechet))

# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:- [2, 3, 4, 5, 6] => [12, 15, 16];- [2, 3, 5, 6] => [12, 15]

# my_list = [2, 3, 4, 5, 6, 7]
# ret = []
# pos = 0
#
# l = len(my_list)
# l_h = math.ceil(l / 2)
#
# while pos < l_h:
#     ret.append(my_list[pos] * my_list[l - pos - 1])
#     pos = pos + 1
#
# print(ret)

# 3. Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# my_list = [7, 1.1, 1.2, 3.1, 5, 10.01]
# ret_max = 0.0
# ret_min = 0.0
# ost = 0.0
#
# l = len(my_list)
# for i in range(l):
#      ost = round(my_list[i] % 1, 2)
#      print(ost)
#
#      if ost == 0:
#          continue
#
#      if ost > ret_max:
#          ret_max = ost
#
#      if ret_min == 0 or ost < ret_min:
#          ret_min = ost
#
# print(ret_max - ret_min)

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# n = int(input ('Введите десятичное число: '))
# k = int(input('Введите количество цифр: '))
#
# def Convert_10_to_2_R(n, k):
#     if n > 0:
#         t = n % 2
#         return Convert_10_to_2_R(n // 2, k + 1) + int(t * math.pow(10, k))
#     else:
#         return 0
#
# print(Convert_10_to_2_R(n, k))

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:  для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

number=int(input('Задайте целое число: '))
max_item=[]
def fibonacci(number):
    if number:
        return 0
    elif number:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)
for count in range(number):
        print(fibonacci(number), )


# Не понял как сделать последнее задание.












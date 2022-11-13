# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
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



def sum_odd_index(lst):
    s = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            s += lst[i]
    print(f"Сумма равна: {s}")

lst = [2, 3, 5, 9, 3]
sum_odd_index(lst)
lst = list(map(int, input("Введите числа через пробел:\n").split()))
sum_odd_index(lst)

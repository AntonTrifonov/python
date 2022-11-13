# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# num = int(input('Введите любое число: '))

# sum = 0

# while num > 0:
#     digit = num % 10
#     sum = sum + digit
#     num = num // 10

# print('Сумма чисел:', sum)


import functools

n = input('Введите любое число: ')
n = [int(digit) for digit in n]

suma = sum(n)

print("Сумма:", suma)
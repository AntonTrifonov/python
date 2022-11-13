# Задайте список из n чисел последовательности (1+\n)^n и выведите на экран их сумму.
# Пример: Для n = 6: {1: 2, 2: 2,25, 3: 2,37, 4: 2,44, 5: 2,49, 6: 2,52}

# n=int(input('Введите число n: '))
# my_dict={}
# summa=0
# for i in range (1,n+1):
#     my_dict[i] = round((1 + 1 / i) ** i, 2)
#     summa = summa + my_dict[i]
#     print(my_dict)
#     print(summa)


n = int(input('Введите число n: '))
lst = [round((1 + 1 / i) ** i, 3) for i in range(1, n + 1)]
print(f'Последовательность: {lst}\nСумма: {round(sum(lst), 3)}')

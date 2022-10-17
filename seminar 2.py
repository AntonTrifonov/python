# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


# from curses.ascii import isdigit

# num = input('Введите число: ')

# suma = 0

# for digit in num:
#     if digit.isdigit():
#         suma += int(digit)

# print("Сумма чисел: ", suma)


# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# num = int(input('Введите число: '))
# a = 1
# for i in range(1, num+1):
#     a = i * a
#     print(a, end=' ')


# 3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# num = int(input('Введите число n: '))

# dict = {}

# for i in range(1, num+1):
#     dict[i]=((1+1/i)**i, 3)
#     summa = summa + dict[i]
#     print(dict)
#     print(summa)



# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# Реализуйте алгоритм перемешивания списка.

from random import randint 


def make_list(n): 
    rand_list = [randint(-n, n)] 
    for i in range(1, n):
        rand_list.append(randint(-n, n)) 
    return rand_list 


def write_file(k, n):
    with open('file.txt', 'w') as file: 
        for i in range(k): #
            file.write(f'{randint(0, n - 1)}\n') 


def get_position(): 
    path = 'file.txt'
    position = open(path, 'r') 
    pos_element = [] #
    for line in position: #
        pos_element.append(int(line)) 
    print(f'Позиции элементов: {pos_element}') 
    position.close() 
    return pos_element 


def product_elements(num_list): 
    position = get_position() 
    product = 1 
    for pos in position: 
        product *= num_list[int(pos)] 
    return product 


num_n = int(input('Количество элементов: N = '))  
num_pos = int(input('Количество множителей: k = ')) 
new_list = make_list(num_n) 
write_file(num_pos, num_n) 
print(f'Заданный список: {new_list}') 
print(f'Произведение элементов на заданных позициях = {product_elements(new_list)}') 




# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным
 
# num = int(input('Введите число - '))
# if (num < 1 or num > 7):
#     print ('None')
# if (num > 1 and num < 6):
#     print ('Будний день')
# if (num == 6 or num == 7):
#     print ('Выходной')


# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

# x=int(input('Введите число x'))
# y=int(input('Введите число y'))
# z=int(input('Введите число z'))
# def logic_function (x, y, z):
#     return (not (x or y or z)) == (not x and not y and not z)
# print(f'значение {logic_function(x,y,z)}')


# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# cor1=int(input('Значение для координаты x не не равная 0'))
# cor2=int(input('Значение для координаты н не не равная 0'))
# if cor1 > 0 and cor2 > 0:
#     print('1 координатная четверть')
# elif cor1 < 0 and cor2 > 0:
#     print('2 координатная четверть')
# elif cor1 < 0 and cor2 < 0:
#     print('3 координатная четверть')
# elif cor1 > 0 and cor2 < 0:
#     print('4 координатная четверть') 


# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# a = int(input('Введите номер координатной четверти'))
# if a == 1:
#     print('Значения X и Y находятся > 0')
# elif a == 2:
#     print('Значения Y находятся > 0, значение X < 0')
# elif a == 3:
#     print('Значения X и Y находятся < 0') 
# elif a == 4:
#     print('Значения Y находятся < 0, значение X > 0')


# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# from math import sqrt

# x1 = int(input('Введите координаты X для точки А'))
# y1 = int(input('Введите координаты Y для точки А'))
# x2 = int(input('Введите координаты X для точки B'))
# y2 = int(input('Введите координаты Y для точки B'))
# print (sqrt((x2-x1)**2+(y2-y1)**2))

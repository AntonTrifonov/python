# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


# str = input('Введите строку: ').replace('абв', '').split(' ')
# result = ' '.join(list(filter(lambda x: x != '', str)))
# print(result)


# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 202 конфеты. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""




# 3. Создайте программу для игры в ""Крестики-нолики"".

# Цикл игры для одного раунда в крестики нолики
 
def mytictactoe(val): 
    print("\n") 
    print("\t     |     |") 
    print("\t  {}  |  {}  |  {}".format(val[0], val[1], val[2])) 
    print('\t_____|_____|_____') 
  
    print("\t     |     |") 
    print("\t  {}  |  {}  |  {}".format(val[3], val[4], val[5])) 
    print('\t_____|_____|_____') 
  
    print("\t     |     |") 
  
    print("\t  {}  |  {}  |  {}".format(val[6], val[7], val[8])) 
    print("\t     |     |") 
    print("\n") 

# Функция для одиночной игры
 
def singlegame(curplayer): 
    # представление игры 
    val = [' ' for i in range(9)] 
      
    # Сохранение позиций занятых X и O 
    playerpos = {'X' : [], 'O' : []} 

while True:
    mytictactoe(val)

    # Блок для ввода хода 
try: 
    print("Player ", curplayer, " turn. Choose your Block : ", end="") 
    chance = int(input()) 
except ValueError: 
    print("Invalid Input!!! Try Again") 
    continue 
 
# Sanity check for CHANCE input 
if chance < 1 or chance > 9: 
    print("Invalid Input!!! Try Again") 
    continue 
  
# Checking if the block is not occupied already 
if val[chance - 1] != ' ': 
    print("Oops! The Place is already occupied. Try again!!") 
    continue 



# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
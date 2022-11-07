# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

str = input('Введите строку: ').replace('абв', '').split(' ')
result = ' '.join(list(filter(lambda x: x != '', str)))
print(result)
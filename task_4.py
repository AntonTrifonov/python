# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0


from random import randint, sample

max_degree = randint(2, 5)
print(max_degree)
def coeffs_list(d):
    coeffs = [randint(0, 10) for i in range(max_degree + 1)]
coeffs = sample(range(9), max_degree)
while coeffs[0] == 0:
    coeffs[0] = randint(1, 10)
print('coeffs', coeffs)

poly = ''
p = max_degree
for i in coeffs:
    poly += f'{i}x^{p-1} + '
    p = p-1
poly += '= 0'
poly = poly.replace('^1', '')
poly = poly.replace('x^0 +', '')

print(poly)
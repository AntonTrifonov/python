# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input('Введите число: '))
prime_numbers_list = []
for i in range(2, number+1):
    for j in prime_numbers_list:
        if i % j == 0:
            break
    else:
        prime_numbers_list.append(i)
print(prime_numbers_list)

primes_list = []
for p_n in prime_numbers_list:
    while number % p_n == 0:
        number = number / p_n
        primes_list.append(p_n)

print(f'Простые множители числа {number} = {primes_list}')
# 2. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа
# in
# 54
# out
# [2, 3, 3, 3]
# in
# 9990
# out
# [2, 3, 3, 3, 5, 37]
# in
# 650
# out
# [2, 5, 5, 13]

def search_common_mult(num):
    div = 2
    some_list = []
    while num > 1:
        if num % div == 0:
            some_list.append(div)
            num /= div
        else:
            div += 1
    return some_list


n = int(input('Введите натуральное число: '))

print(f'Список простых множителе числа {n}:\n{search_common_mult(n)}')

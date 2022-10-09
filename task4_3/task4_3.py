# 3. Задайте последовательность чисел. 
# Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
# in
# -1
# out
# Negative value of the number of numbers!
# []
# in
# 10
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

from random import randrange


def rand_num(count: int):
    if count < 0:
        print('Не может быть такого количества элементов')
        return []

    some_list = []
    for i in range(count):
        some_list.append(randrange(count))

    return some_list


def find_elem(some_list: list):
    res = []
    new_dict = {}.fromkeys(some_list, 0)

    for i in some_list:
        new_dict[i] += 1

    for j in new_dict:
        if new_dict[j] == 1:
            res.append(j)

    return res


n = int(input('Введите количество чисел: '))

new_list = rand_num(n)
print(f'Список неповторяющихся элементов последовательности {new_list}:\n{find_elem(new_list)}')

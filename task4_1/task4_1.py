# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000
# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001
# out
# 8.988

from decimal import Decimal


def rounding(num, accuracy):
    n = Decimal(f'{num}')
    return n.quantize(Decimal(f'{accuracy}'))


number = float(input('Введите вещественное число: '))
d = float(input('Введите точность округления 0.0001: '))

print(rounding(number, d))

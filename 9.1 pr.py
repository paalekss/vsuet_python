# Вариант 2

# 2.1 Дано натуральные числа a,b Вычислить остаток от деления a на b.

def division(a, b):

    return division(a - b, b) if a >= b else a

a = int(input('Введите натуральное число a: '))
b = int(input('Введите натуральное число b: '))

result = division(a, b)
print(result)


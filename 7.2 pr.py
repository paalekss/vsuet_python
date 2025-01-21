# Вариант 2

# 2.2 Пользователь вводит две стороны трех прямоугольников.
# Вывести их площади.

def square_p(a, b):
    return a * b

first_a, first_b = map(int, input('Введите стороны первого прямоугольника: ').split())
second_a, second_b = map(int, input('Введите стороны второго прямоугольника: ').split())
third_a, third_b = map(int, input('Введите стороны третьего прямоугольника: ').split())

print('\nПлощадь первого прямоугольника: ' + str(square_p(first_a, first_b)))
print('Площадь второго прямоугольника: ' + str(square_p(second_a, second_b)))
print('Площадь третьего прямоугольника: ' + str(square_p(third_a, third_b)))

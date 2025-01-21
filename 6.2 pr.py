# Вариант 2

# 2.1 Дан массив целых чисел.
# Переписать все положительные элементы во второй массив, а остальные - в третий.

from random import *
N = int(input('Введите размер массива: '))
l = [randint(-100, 100) for i in range(N)]
print(l)

x = []
y = []
for i in range(N):
    if l[i] > 0:
        x.append(l[i])
    elif l[i] < 0:
        y.append(l[i])
        
print(f'Массив положительных элементов: \n{str(x)}')
print(f'Массив отрицательных элементов: \n{str(y)}')

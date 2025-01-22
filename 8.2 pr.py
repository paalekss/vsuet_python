# Вариант 2

# 2.2 Дана прямоугольная матрица A[N][N].
# Переставить первый и последний столбцы местами и вывести на экран.

from random import randint

def replace_columns(matrix, n):

    for i in range(n):
        t = matrix[i][0]
        matrix[i][0] = matrix[i][n - 1]
        matrix[i][n - 1] = t

    return matrix

n = int(input('Введите размер прямоугольной матрицы A[N][N]: '))
A = []
for i in range(n):
    b = []
    for j in range(n):
        b.append(randint(-100, 100))
    A.append(b)

print('Исходный массив: \n')
for i in range(n):
    for j in range(n):
        print(A[i][j], end = ' ')
    print()

A = replace_columns(A, n)

print('Измененный массив: \n')
for i in range(n):
    for j in range(n):
        print(A[i][j], end = ' ')
    print()
    


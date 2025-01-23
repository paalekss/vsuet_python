# Вариант 2

# 2.2 Дана прямоугольная матрица A[N][N].
# Переставить первый и последний столбцы местами и вывести на экран.

from random import randint

def read_matrix(filename_vvod):
    with open(filename_vvod, 'r') as file:
        matrix = [list(map(int, line.split())) for line in file]
    return matrix

def write_in_file(filename_vivod, result, n):
    with open(filename_vivod, 'w') as file:
        for i in range(n):
            str_row = ''
            for j in range(n):
                str_row += str(result[i][j]) + ' '
            file.write(str_row + '\n')

def replace_columns(matrix, n):

    for i in range(n):
        t = matrix[i][0]
        matrix[i][0] = matrix[i][n - 1]
        matrix[i][n - 1] = t

    return matrix

filename_vvod = 'ПудиноваАВ_ЗИТ-24м_vvod1.txt'
A = read_matrix(filename_vvod)
n = len(A)

A = replace_columns(A, n)

filename_vivod = 'ПудиноваАВ_ЗИТ-24м_vivod1.txt'
write_in_file(filename_vivod, A, n)
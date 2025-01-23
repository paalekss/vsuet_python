# Вариант 2

# 2.1 Дана целая квадратная матрица n-го порядка.
# Определить, является ли она магическим квадратом, т.е. такой матрицей,
# в которой суммы элементов во всех строках и столбцах одинаковы.

def read_matrix(filename_vvod):
    with open(filename_vvod, 'r') as file:
        matrix = [list(map(int, line.split())) for line in file]
    return matrix

def write_in_file(filename_vivod, result):
    with open(filename_vivod, 'w') as file:
        file.write(result)

def is_magic_matrix(matrix, n):

    result = True
    sum_el = 0
    for i in range(n):
        sum_el += matrix[0][i]
    i = 1
    for i in range(n):
        sum_row = 0
        for j in range(n):
            sum_row += matrix[i][j]
        if sum_row != sum_el:
            result = False
    i = 0
    for i in range(n):
        sum_col = 0
        for j in range(n):
            sum_col += matrix[i][j]
        if sum_col != sum_el:
            result = False
    if result:
        return 'Это магический квадрат'
    else:
        return 'Это НЕ магический квадрат'

filename_vvod = 'ПудиноваАВ_ЗИТ-24м_vvod.txt'

a = read_matrix(filename_vvod)
n = len(a)

print('Исходный массив:')
for i in range(n):
    for j in range(n):
        print(a[i][j], end = ' ')
    print()

filename_vivod = 'ПудиноваАВ_ЗИТ-24м_vivod.txt'
result = is_magic_matrix(a, n)
write_in_file(filename_vivod, result)
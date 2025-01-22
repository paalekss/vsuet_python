# Вариант 2

# 2.1 Дана целая квадратная матрица n-го порядка.
# Определить, является ли она магическим квадратом, т.е. такой матрицей,
# в которой суммы элементов во всех строках и столбцах одинаковы.

def is_magic_matrix(matrix, n):

    sum_el = 0
    for i in range(n):
        sum_el += matrix[0][i]
    i = 1
    for i in range(n):
        sum_row = 0
        for j in range(n):
            sum_row += matrix[i][j]
        if sum_row != sum_el:
            return False
    i = 0
    for i in range(n):
        sum_col = 0
        for j in range(n):
            sum_col += matrix[i][j]
        if sum_col != sum_el:
            return False

    return True

n = int(input('Введите размер квадратной матрицы: '))
a = []
for i in range(n):
    b = []
    for j in range(n):
        print('Введите [' , i, ',', j, '] элемент: ')
        b.append(int(input()))
    a.append(b)

print('Исходный массив: \n')
for i in range(n):
    for j in range(n):
        print(a[i][j], end = ' ')
    print()

if is_magic_matrix(a, n):
    print('Это магический квадрат')
else:
    print('Это НЕ магический квадрат')    


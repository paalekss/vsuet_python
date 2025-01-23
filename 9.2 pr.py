# Вариант 2

# 2.2 Дана последовательность натуральных чисел (одно число в строке), завершающаяся числом 0.
# Определите значение второго по величине элемента в этой последовательности, то есть элемента, 
# который будет наибольшим ,если из этой последовательности удалить наибольший элемент.

def helper(first_max, second_max):
        num = int(input())
        if num == 0:
            return second_max
        if num > first_max:
            return helper(num, first_max)
        elif num > second_max:
            return helper(first_max, num)
        else:
            return helper(first_max, second_max)

def find_second_max():
    
    first_num = int(input('Введите числа: \n'))
    if first_num == 0:
        return False 
    second_num = int(input())
    if second_num == 0:
        return False
    
    if first_num > second_num:
        return helper(first_num, second_num)
    else:
        return helper(second_num, first_num)

second_max = find_second_max()
if second_max != False:
    print('Второй по величине элемент: ', second_max)
else:
    print('Чисел в последовательности, не считая 0, должно быть минимум двое')
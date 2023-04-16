# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
nums_elem = int(input("Enter the number of elemens in array: "))
array = [random.randint(1, 20) for _ in range(nums_elem)]
set_num = int(input("Enter the setting number: "))
print(array)
position = 0
dif = 100 # максимальная разность
for i in range(0, len(array)):
    result = abs(set_num - array[i])
    if dif > result:
        position = i
        dif = result

print(f"Closest element to {set_num} is {array[position]}")







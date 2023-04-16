# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

nums_elem = int(input("Enter the number of elemens in array: "))
array = [int(i) for i in input().split()]
unkn_num = int(input("Enter the unknown number: "))

print(f"The number {unkn_num} occurs in array {array.count(unkn_num)} times")


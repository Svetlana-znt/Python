# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно 
# ввести с клавиатуры. Формула для получения n-го члена 
# прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

n = int(input("Введите количество элементов = "))
d = int(input("Введите разность = "))
a1 = int(input("Введите первый член прогрессии = "))

for i in range(n):
   print(a1 + i*d)

#Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# list_1 = [-2, 12, 1, 3, 8, 16, 0, -5, 7, 10, 2, -5, 4, -2]
# min_number = int(input("Введите минимальное число = "))
# max_number = int(input("Введите максимальное число = "))
# for i in range(len(list_1)):
#     if min_number <= list_1[i] <= max_number:
#         print(i)
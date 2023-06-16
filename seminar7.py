# L = [1, 2, 3, 4]

# print(list(map(lambda x: x**2, L)))
#--------------------------------------------------------------------

#print(list(filter(lambda x: x % 2 == 0, [1, 3, 2, 5, 20, 21])))

#-----------------------------------------------------------------
# lines = ["abcd", "ab", "ba", "acde"]
# print(sorted(lines, key=lambda line: (len(line), line)))
#-------------------------------------------------------------------------
# employee_numbers = [2, 9, 18, 28]
# employee_names = ["Дима", "Марина", "Андрей", "Никита"]

# zipped_values = zip(employee_names, employee_numbers)
# zipped_list = list(zipped_values)

# print(zipped_list)
#----------------------------------------------------------------------
# Задача №49. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты.
#-----------------------------------------------------------------------
# orbits = [(1,3), (1.5, 10), (7, 2), (6, 6), (4, 3)]

# def orbit_max(orbits):
#     orb = list(filter(lambda x: x[0] != x[1], orbits))
#     return max(map(lambda x: x[0]*x[1], orb))

# n = orbit_max(orbits)
# print(n)
#--------------------------------------------------------------------------

# Задача 51. Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так. 
#--------------------------------------------------------------------------
# def same_by(fun, objects):
#     for item in objects:
#         if not fun(item):
#             return False
#     return True

# values = [0, 2, 10, 6]

# if same_by(lambda x: x%2 == 0, values):
#     print("same")
# else:
#     print("different")
#--------------------------------------------------------------------------------

#ДЗ. Задача 34
# def rhythm(str):
#     str = str.split()
#     list_1 = []
#     for word in str:
#         sum_w = 0
#         for i in word:
#             if i in 'аеёиоуыэюя':
#                 sum_w += 1
#         list_1.append(sum_w)
#     return len(list_1) == list_1.count(list_1[0])


# str_1 = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# if rhythm(str_1):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')
    
#----------------------------------------------------------------------------------------------
# ДЗ Задача 36

def print_operation_table(operation, num_rows, num_columns):
    a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    for i in a:
        print(*[f"{x:>4}" for x in i])


line = int(input("Введите количество строк: "))
columns = int(input("Введите количество столбцов: "))
print_operation_table(lambda x,y: x*y,line,columns)




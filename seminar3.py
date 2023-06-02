# list_new = list() # Создаем пустой список
# for i in range(8): # Цикл выполняется 8 раз
#     n = int(input('Введите чило:')) # Пользователь вводит целое число
#     list_new.append(n) # Сохранение целого числа в конце списка
# print(list_new)
# count = 0
# max = 0
# for j in range(0,len(list_new)-1):
#     for k in range(j+1,len(list_new)):
#         if list_new[j]  != list_new[k]:
#             count +=1
#     # if count > max:
#     #     max = count
#         print(count)
#------------------------------------------------------------------------------
# k = int(input("введите число сдвига k = "))
# list_new = [1,2,3,5,8,9,12,4]
# list_1=list()
# j = 0
# for i in range (len(list_new)):
#     if i<=k:
#         j=len(list_new)-i
#         list_1[j] = list_new[i]
#     elif i > k:
#         list_1[j] = list_new[i]
#         j+=1
# print(list_1)
#--------------------------------------------------------------------------
#ДЗ №16
# N = int(input("Введите количество элементов в списке = "))
# list_new = list()

# for i in range(N):
#     n = int(input("Введите значение = "))
#     list_new.append(n)
# print(list_new)

# x = int(input("Введите значение элемента Х = "))
# count = 0

# for j in range(N):
#     if list_new[j] == x:
#         count+=1
# print(count)
#-----------------------------------------------------------------------
#ДЗ №18
# N = int(input("Введите количество элементов в списке = "))
# list_new = list()

# for i in range(N):
#     n = int(input("Введите значение = "))
#     list_new.append(n)
# print(list_new)

# x = int(input("Введите значение элемента Х = "))
# count = 0
# d1 = 10


# for j in range(N):
#     if abs(list_new[j]-x) < d1 or abs(list_new[j]-x) == d1:
#         count = j
#         print(count)
#         d1 = abs(list_new[j]-x)
#---------------------------------------------------------------------------
#
# dictionary = {1:"AEIOULNSTRАВЕИНОРСТ",
#                 2:"DGДКЛМПУ",
#                 3:"BCMPБГЁЬЯ",
#                 4:"FHVWYЙЫ",
#                 5:"KЖЗХЦЧ",
#                 8:"JXШЭЮ",
#                 10:"QZФЩЪ"}

# word = input("Введите слово: ").upper()
# summ = 0
# for i in word:
#     for k, v in dictionary.items():
#         if i in v:
#             summ += k
# print(f"Стоимость слова: {summ}")





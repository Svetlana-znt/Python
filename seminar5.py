#------------------------------------------------------------------------
# Задача 31
# n = int(input("Введите номер элемента последовательности Фибоначчи = "))

# def fib(n):
#     if n == 0 or n == 1:
#         return n
    
#     return fib(n-2) + fib (n-1)

# print(fib(n))
#------------------------------------------------------------------------
# Задача 33   
# list = [1, 2, 3, 4, 2, 5]
# minimum = 5
# maximum =1

# for i in range(len(list)):
#     if list[i] < minimum:
#         minimum = list[i]

# print(minimum)

# for i in range(len(list)):
#     if list[i] > maximum:
#         maximum = list[i]

# print(maximum)

# for i in range((len(list))):
#     if list[i] == maximum:
#         list[i] = minimum

# print(list)
#-------------------------------------------------------------------------
# Задача 35
a = int(input("Введите число = "))
enter = "True"
i = 2
while i < a:
    if a % i != 0:
        i+=1
    else:
        enter = "False"
        break
print(enter)
#----------------------------------------------------------------------------
#  ДЗ Задача 26

# a = int(input("Введите целое число = "))
# b = int(input("Введите степень числа  = "))

# def power(a, b):
#     if b == 0:
#         return 1
#     return a * power(a, b-1)
# print(power(a,b))

#-------------------------------------------------------------------------

# ДЗ Задача 28

# a = int(input("Введите неотрицательное число = "))
# b = int(input("Введите неотрицательно число = "))

# def summ(a, b):
#     if a == 0:
#         return b

#     return summ(a-1, b+1)

# print(summ(a, b))

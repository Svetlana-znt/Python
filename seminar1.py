# ------------------------------------------------------------------------
# Найдите сумму цифр трехзначного числа 
# --------------------------------------------------------------------------
# print("Введите число: ")
# n = int(input("n = "))
# sum = 0
# if 99<n<=1000:
#     while n!=0:
#        sum = sum + n%10
#        n = n//10
#     print(f"Сумма равна {sum}")
# else:
#     print("Введено не трехзначное число")
#--------------------------------------------------------------------------
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
#----------------------------------------------------------------------------
# print("Количество журавликов у Пети и у Сережи = ")
# p = int(input())
# print(2*p + 4*p)
#----------------------------------------------------------------------------
#Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
#---------------------------------------------------------------------------
# print("Введите номер билета  = ")
# b = int(input())
# i=0
# sum1=0
# sum2=0
# while i<3:
#     sum1 = sum1 + b%10
#     i+=1
#     b = b//10
# else: 
#     while i>=3 and i<6:
#         sum2 =sum2 + b%10
#         b=b//10
#         i+=1
# print(sum1)
# print(sum2)
# if sum1 == sum2:
#     print("True")
# else:
#     print("False")
#---------------------------------------------------------------------
#Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
#---------------------------------------------------------------------
print("Введите n = ")
n = int(input())
print("Введите m = ")
m = int(input())
print("Введите k = ")
k = int(input())
if (k==n and k!=n*m) or (k==m and k!=n*m):
    print("yes")
else:
    print("no")








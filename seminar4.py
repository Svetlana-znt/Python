# ДЗ №22
import random
kust = int(input("введите количество кустов: "))
berryes = list(random.randint(0, 10) for i in range(kust))
result = []
i = 0
sum = 0

print(berryes)

while (i < kust):
    if (i == kust - 1):
        sum = berryes[i] + berryes[i - 1] + berryes[0]
    else:
        sum = berryes[i] + berryes[i - 1] + berryes[i + 1]
        result.append(sum)
        result.sort()
    i += 1

print(f"максимальное число ягод за одну итерацию {result[-1]}")
#---------------------------------------------------------------------
# ДЗ №24
# from random import randint
# n_set = set(randint(1, 20) for i in range(int(input("Введите кол-во элементов первого множества: "))))
# print(n_set)
# m_set = set(randint(1, 20) for i in range(int(input("Введите кол-во элементов второго множества: "))))
# print(m_set)
# s_set = sorted(n_set.intersection(m_set))
# print(s_set)

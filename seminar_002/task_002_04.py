# 4 – Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
import random

n = int(input('n = '))
num_list = []

for i in range(n):
    num_list.append(random.randint(-n, n))

file = open("file.txt")
indexes = []

for line in file.readlines():
    indexes.append(int(line))

multi = 1

for i in indexes:
    if i <= n - 1:
        multi *= num_list[i]

print(multi)



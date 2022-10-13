# 1 – Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

n = str(input())
sum_of_numbers = 0

for char in n:
    if char.isnumeric():
        sum_of_numbers += int(char)

print(sum_of_numbers)

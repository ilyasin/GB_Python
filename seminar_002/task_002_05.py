# 5 – Реализуйте алгоритм перемешивания списка.
import random

size = int(input('size = '))
num_list = []

for i in range(size):
    num_list.append(random.randint(0, 100))

print(num_list)
random.shuffle(num_list)
print(num_list)

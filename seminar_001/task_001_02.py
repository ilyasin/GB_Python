# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = False
y = False
z = False

for x in False, True:
    for y in False, True:
        for z in False, True:
            statement = not(x or y or z) == (not x and not y and not z)
            print(f'{x}, {y}, {z} -> {statement}')

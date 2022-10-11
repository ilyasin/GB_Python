# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def check_statement():
    x = False
    y = False
    z = False
    statement = True

    for x in False, True:
        for y in False, True:
            for z in False, True:
                statement = not(x or y or z) == (not x and not y and not z)
                if not statement:
                    return statement

    return statement


print(check_statement())

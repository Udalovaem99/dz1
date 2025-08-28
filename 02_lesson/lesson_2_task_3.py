import math


def square(side):
    return math.ceil(side*side)


side = int(input("Сторона: "))
print(f"Площадь равна:{square(side)}")

def plus(x, y):
    z = int(x) + int(y)
    return print("Сумма", z)


def minus(x, y):
    z = int(x) - int(y)
    return print("Разность", z)


a = input("1 число ")
b = input("2 число ")

plus(a, b)
minus(a, b)

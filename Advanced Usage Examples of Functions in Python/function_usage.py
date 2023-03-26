def square(x):
    return x ** 2


def cube(x):
    return x ** 3


def operate(func, x):
    return func(x)


print(operate(square, 5))  # 25
print(operate(cube, 5))  # 125


# Return functions as values from another function
def get_operation(power):
    if power == 2:
        return square
    else:
        return cube


operation = get_operation(2)
print(operation(5))  # 25

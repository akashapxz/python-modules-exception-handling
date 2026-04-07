def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid data type"


def square_root(num):
    import math
    try:
        return math.sqrt(num)
    except ValueError:
        return "Error: Cannot find sqrt of negative number"
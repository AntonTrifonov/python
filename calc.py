def make_sum(a, b):
    return a + b


def make_sub(a: float, b: float) -> float:
    return a - b


def make_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Error by b = 0'


def make_mult(a, b):
    return a * b

# numerical_integration.py
# describes:
# 1) middle rectangle method
# 2) trapezium method
# 3) simpson method


def mid_rectangle_method(a, b, f, n):
    step = (b - a) / n
    s = 0
    for i in range(0, n):
        s += step * f(a + (i + 0.5) * step)
    return s


def trapezium_method(a, b, f, n):
    step = (b - a) / n
    s = 0
    for i in range(0, n):
        s += step * (f(a + i * step) + f(a + (i + 1) * step)) / 2
    return s


def simpson_method(a, b, f, n):
    step = (b - a) / n
    s = f(a) + f(b)
    for i in range(0, n):
        s += 4 * f(a + (i + 0.5) * step)
    for i in range(1, n):
        s += 2 * f(a + i * step)
    return (step / 6) * s



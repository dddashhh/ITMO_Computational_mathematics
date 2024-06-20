import math


def left_rectangle_rule(f, a, b, n, order = 1):
    h = (b - a) / n
    integral = 0
    for i in range(n):
        integral += f(a + i * h)
    integral *= h
    return integral, order


def right_rectangle_rule(f, a, b, n, order = 1):
    h = (b - a) / n
    integral = 0
    for i in range(1, n + 1):
        integral += f(a + i * h)
    integral *= h
    return integral, order


def mid_rectangle_rule(f, a, b, n, order = 2):
    h = (b - a) / n
    integral = 0
    for i in range(n):
        integral += f(a + (i + 0.5) * h)
    integral *= h
    return integral, order


def trapezoidal_rule(f, a, b, n, order = 2):
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        integral += f(a + i * h)
    integral *= h
    return integral, order


def simpsons_rule(f, a, b, n, order = 4):
    h = (b - a) / n
    integral = f(a) + f(b)
    for i in range(1, n):
        if i % 2 == 0:
            integral += 2 * f(a + i * h)
        else:
            integral += 4 * f(a + i * h)
    integral *= h / 3
    return integral, order


def runge_rule(prev_integral, cur_integral, order):
    return abs(cur_integral - prev_integral) / ((2 ** order) - 1)

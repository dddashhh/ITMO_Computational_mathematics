import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


def find_roots(equation_function, range_start, range_end, step=0.0001):
    roots = []
    current_x = range_start
    while current_x <= range_end:
        y1 = equation_function(current_x)
        current_x += step
        y2 = equation_function(current_x)
        if y1 * y2 <= 0:
            roots.append(current_x)
    return roots


def find_extrema(func, start, end):
    x = np.linspace(start, end, 1000)
    y = func(x)
    peaks, _ = find_peaks(y)
    valleys, _ = find_peaks(-y)
    extrems = []
    for peak in peaks:
        extrems.append(x[peak])
    for valley in valleys:
        extrems.append(x[valley])
    return extrems


def bisection_method(func, a, b, epsilon=1e-6, max_iterations=10, derive_f=lambda x: np):
    iterations = 0
    c = (a + b) / 2
    while abs(func(c)) > epsilon:
        c = (a + b) / 2
        if abs(func(c)) <= epsilon:
            break
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
        iterations += 1
    # print("---------", (b - a) / 2)
    return c, iterations, func(c)


def secant_method(func, a, b, epsilon=1e-6, max_iter=100, derive_f=lambda x: np):
    xi = a
    xii = b
    iterations = 0

    while abs(xi - xii) > epsilon and iterations < max_iter:
        x_next = xi - func(xi) * (xii - xi) / (func(xii) - func(xi))
        xi, xii = xii, x_next
        iterations += 1
        if abs(func(x_next)) <= epsilon:
            break
    return x_next, iterations, func(x_next)


def check_convergence(f, a, b):
    if (abs(1 + 1 / max(abs(f(a)), abs(f(b))) * f(a)) < 1) and (abs(1 + 1 / max(abs(f(a)), abs(f(b))) * f(b)) < 1):
        print("Условие сходимости метода простой итерации на выбранном интервале выполнено")
        pass
    else:
        print("Условие сходимости метода простой итерации на выбранном интервале не выполнено")


def simple_iterations_method(func, a, b, epsilon=1e-6, max_iter=1000, derive_f=lambda x: np):
    iter_count = 0
    x0 = b
    if derive_f((a + b) / 2) < 0:
        L = 1 / max(abs(derive_f(a)), abs(derive_f(b)))
    else:
        L = -1 / max(abs(derive_f(a)), abs(derive_f(b)))
    # print('L----', L, derive_f (a), derive_f(b))
    while iter_count < max_iter:
        x1 = x0 + L * func(x0)
        # print(iter_count, x1, func(x1))
        if abs(x1 - x0) < epsilon:
            return x1, iter_count, func(x1)
        x0 = x1
        iter_count += 1
    print("Решение не сходится после {} итераций".format(max_iter))
    return x0, iter_count, func(x0)


def jacobian(f, x, h=1e-6):
    n = len(x)
    J = np.zeros((n, n))
    f0 = f(x)

    for i in range(n):
        x_plus_h = x.copy()
        x_plus_h[i] += h
        J[:, i] = (f(x_plus_h) - f0) / h

    return J


def newton_method(f, x0, epsilon=1e-6, max_iter=100):
    x = x0
    iterations = 0
    errors = []
    for _ in range(max_iter):
        J = jacobian(f, x)
        delta_x = np.linalg.solve(J, -f(x))
        x = x + delta_x
        errors.append(np.linalg.norm(delta_x))
        iterations += 1
        if (abs(delta_x[0])< epsilon) and (abs(delta_x[1])< epsilon):
            break

    return x, iterations, errors


def plot_function(func, a, b, roots=[]):
    x = np.linspace(a - 5, b + 5, 100)
    y = func(x)

    plt.plot(x, y)
    plt.scatter(roots, [0] * len(roots), color='pink')
    plt.title("Graph of the function")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()
    plt.show()


def plot_system(Z1, Z2, result):
    x_values = np.linspace(-2, 2, 400)
    y_values = np.linspace(-2, 2, 400)
    X, Y = np.meshgrid(x_values, y_values)
    plt.figure()
    plt.contour(X, Y, Z1, levels=[0])
    plt.contour(X, Y, Z2, levels=[0])
    plt.plot(result[0], result[1], 'ro')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График системы нелинейных уравнений')
    plt.show()

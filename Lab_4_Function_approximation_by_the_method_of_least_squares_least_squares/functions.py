import numpy as np
import matplotlib.pyplot as plt


def read_data(filename=None):
    if filename:
        try:
            with open(filename, 'r') as f:
                data = [line.strip().split() for line in f]
            x = np.array([float(row[0]) for row in data])
            y = np.array([float(row[1]) for row in data])
        except FileNotFoundError:
            print(f"Файл '{filename}' не найден. Вместо этого используйте ввод с консоли")
            x = []
            y = []
            while True:
                try:
                    input_str = input("Введите значения x,y (разделенные запятой): ")
                    if input_str.lower() == 'q':
                        break
                    x_val, y_val = map(float, input_str.split(','))
                    x.append(x_val)
                    y.append(y_val)
                except ValueError:
                    print("Неверный ввод. Пожалуйста, введите значения x,y разделенные запятой")
            x = np.array(x)
            y = np.array(y)
    else:
        x = []
        y = []
        while True:
            try:
                input_str = input("Введите значения x,y (разделенные запятой): ")
                if input_str.lower() == 'q':
                    break
                x_val, y_val = map(float, input_str.split(','))
                x.append(x_val)
                y.append(y_val)
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите значения x,y разделенные запятой")
        x = np.array(x)
        y = np.array(y)
    return x, y


def calculate_deviation(x, y, f):
    return np.sum((f(x) - y) ** 2)


def linear_function(x, a, b):
    return a * x + b


def quadratic_function(x, a, b, c):
    return a * x ** 2 + b * x + c


def cubic_function(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d


def exponential_function(x, a, b):
    return a * np.exp(b * x)


def logarithmic_function(x, a, b):
    return a * np.log(x) + b


def power_function(x, a, b):
    return a * (x) ** b


def least_squares_fit(x, y, function):
    n = len(x)
    if function == linear_function:
        # Linear function: y = ax + b
        A = np.vstack([x, np.ones(n)]).T
        coeffs, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
        a, b = coeffs
        f_fitted = linear_function(x, a, b)
        # print(A)
    elif function == quadratic_function:
        # Quadratic function: y = ax^2 + bx + c
        A = np.vstack([x ** 2, x, np.ones(n)]).T
        coeffs, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
        a, b, c = coeffs
        f_fitted = quadratic_function(x, a, b, c)
    elif function == cubic_function:
        # Cubic function: y = ax^3 + bx^2 + cx + d
        A = np.vstack([x ** 3, x ** 2, x, np.ones(n)]).T
        coeffs, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
        a, b, c, d = coeffs
        f_fitted = cubic_function(x, a, b, c, d)
    elif function == exponential_function:
        # Exponential function: y = a * exp(bx)
        A = np.vstack([np.exp(x), np.ones(n)]).T
        coeffs, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
        a, b = coeffs
        f_fitted = exponential_function(x, a, b)
    elif function == logarithmic_function:
        # Logarithmic function: y = a * log(x) + b
        A = np.vstack([np.log(x), np.ones(n)]).T
        coeffs, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
        a, b = coeffs
        f_fitted = logarithmic_function(x, a, b)
    elif function == power_function:
        # Power function: y = a * x^b
        A = np.vstack([x, np.log(x)]).T
        coeffs, _, _, _ = np.linalg.lstsq(A, np.log(y), rcond=None)
        a, b = coeffs
        f_fitted = power_function(x, np.exp(a), b)
        print(A)
    else:
        raise ValueError("Неверный тип функции")
    rms_error = np.sqrt(np.mean((y - f_fitted) ** 2))
    return [float(i) for i in coeffs], rms_error


def pearson_correlation(x, y):
    return np.corrcoef(x, y)[0, 1]

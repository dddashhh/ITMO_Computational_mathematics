import numpy as np

from functions import *


if __name__ == "__main__":
    filename = input("Введите название файла (или оставьте пустым для консольного ввода): ")
    x, y = read_data(filename)

    functions = [
        linear_function,
        quadratic_function,
        cubic_function,
        exponential_function,
        logarithmic_function,
        power_function,
    ]

    best_function = None
    min_rms_error = float('inf')
    results = {}

    for function in functions:
        coeffs, rms_error = least_squares_fit(x, y, function)
        if function == power_function:
            results[function] = {
                'coeffs': [np.exp(coeffs[0]), coeffs[1]],
                'rms_error': rms_error,
                'f_fitted': function(x, np.exp(coeffs[0]), coeffs[1]),
            }
        else:
            results[function] = {
                'coeffs': coeffs,
                'rms_error': rms_error,
                'f_fitted': function(x, *coeffs),
        }

        if rms_error < min_rms_error:
            min_rms_error = rms_error
            best_function = function

    print("---------------------- Результаты ----------------------")
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'o', label='Data')
    for function, result in results.items():
        print(f"Функция: {function.__name__}")
        print(f"Коэффициенты: {[float(i) for i in result['coeffs']]}")
        print(f"Среднеквадратичная ошибка: {result['rms_error']}")
        print()
        if function.__name__ != "exponential_function":
            plt.plot(x, results[function]['f_fitted'], label=f'{function.__name__} Fit')
            plt.xlabel('x')
            plt.ylabel('y')
            plt.legend()
            plt.grid(True)
    plt.show()


    print("----------------------------------------------------")
    print(f"Наилучшая аппроксимирующая функция: {best_function.__name__}")
    print(f"Коэффициенты: {results[best_function]['coeffs']}")
    print(f"Среднеквадратичная ошибка: {results[best_function]['rms_error']}")

    if best_function == linear_function:
        correlation_coeff = pearson_correlation(x, y)
        print(f"Коэффициент корреляции Пирсона: {correlation_coeff}")

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'o', label='Data')
    plt.plot(x, results[best_function]['f_fitted'], label=f'{best_function.__name__} Fit')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Данные и наилучшая аппроксимирующая функция')
    plt.legend()
    plt.grid(True)
    plt.show()

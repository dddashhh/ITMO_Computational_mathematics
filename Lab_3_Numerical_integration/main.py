from functions import *


def equation1(x):
    return x ** 2 - x + 5


def equation2(x):
    return 8 * x ** 7 + 6 * x ** 5 + 4 * x ** 3 - 5 * x ** 2 + 6 * x -7


def equation3(x):
    return math.exp(x) - x


functions = {1: equation1, 2: equation2, 3: equation3}
if __name__ == '__main__':
    print("Выберите функцию для интегрирования:")
    print("1. x^2 - x + 5")
    print("2. 8x^7+6x^5+4x^3-5x^2+6x-7")
    print("3. exp(x) - x")
    choice = int(input("Введите номер выбранной функции: "))

    if choice not in functions:
        print("Некорректный выбор функции.")
    else:
        f = functions[choice]

    lower_bound = float(input("Введите нижний предел интегрирования: "))
    upper_bound = float(input("Введите верхний предел интегрирования: "))
    epsilon = float(input("Введите требуемую точность: "))
    n_input = int(input("Введите начальное число разбиения интервала: "))

    methods = [('Левых прямоугольников', left_rectangle_rule), ('Правых прямоугольников', right_rectangle_rule),
               ('Средних прямоугольников', mid_rectangle_rule), ('Трапеций', trapezoidal_rule), ('Симпсона', simpsons_rule)]

    for method_name, method_func in methods:
        prev_integral = 0
        cur_integral = 0
        n = n_input
        while True:
            prev_integral = cur_integral
            cur_integral, order = method_func(f, lower_bound, upper_bound, n)

            if prev_integral is not None:
                error_estimate = runge_rule(prev_integral, cur_integral, order)
                if error_estimate < epsilon:
                    break
            n *= 2

        print(f"\nМетод: {method_name}")
        print(f"Значение интеграла: {cur_integral}")
        print(f"Число разбиений: {n}")
        print(f"Точность: {epsilon}")
        print()

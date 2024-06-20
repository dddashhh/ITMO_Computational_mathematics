from functions import *


def equation1(x):
    return x ** 2 - 4


def equation2(x):
    return np.sin(x)


def equation3(x):
    return np.exp(x) - 3


def equation4(x):
    return x ** 3 - 5 * x - 9


def equation5(x):
    return np.cos(x) - x


def system1(x):
    eq1 = x[0] ** 2 - x[1] ** 2 - 1
    eq2 = x[0] + x[1] - 3
    return np.array([eq1, eq2])


def system2(x):
    eq1 = x[0] ** 2 + x[1] ** 2 - 4
    eq2 = 3 * x[0] ** 2 - x[1]
    return np.array([eq1, eq2])


if __name__ == '__main__':
    choice = int(
        input("Решить систему или нелинейное уравнение? 1-Нелинейное уравнение 2-Система нелинейных уравнений - "))
    if choice == 1:
        print("Выберите функцию для вычисления:")
        print("1. x^2 - 4")
        print("2. sin(x)")
        print("3. exp(x) - 3")
        print("4. x^3 - 5x - 9")
        print("5. cos(x) - x")

        choice = input("Введите номер выбранной функции: ")

        if choice == '1':
            func = equation1
            deriv_func = lambda x: 2 * x
            f1 = lambda x: 4
            f2 = lambda x: 0

        elif choice == '2':
            func = equation2
            deriv_func = lambda x: np.cos(x)
            f1 = lambda x: - np.sin(x)
            f2 = lambda x: np.cos(x)

        elif choice == '3':
            func = equation3
            deriv_func = lambda x: np.exp(x)
            f1 = lambda x: 3
            f2 = lambda x: -np.exp(x)

        elif choice == '4':
            func = equation4
            deriv_func = lambda x: 3 * x ** 2 - 5
            f1 = lambda x: 10/3 * x + 9
            f2 = lambda x: -16.87

        else:
            func = equation5
            deriv_func = lambda x: -np.sin(x) - 1
            f1 = lambda x: -np.cos(x) + x
            f2 = lambda x: np.sin(x) + 1

        plot_function(func, -10, 10)

        lower_bound = float(input("Введите нижнюю границу интервала: "))
        upper_bound = float(input("Введите верхнюю границу интервала: "))
        extrema = [lower_bound, upper_bound]

        epsilon = float(input("Введите точность: "))

        if upper_bound <= lower_bound:
            print("Неправильно задан интервал")

        roots = []
        methods = [('Половинного деления', bisection_method), ('Секущих', secant_method), ('Простой итерации', simple_iterations_method)]

        count_roots = len(find_roots(func, lower_bound, upper_bound))
        if count_roots != 1:
            plot_function(func, lower_bound, upper_bound, find_roots(func, lower_bound, upper_bound))
            print(f"На выбранном интервале [{lower_bound}; {upper_bound}] {count_roots} корней")

            if count_roots > 1:
                print(f"Предлагаем разбить ваш интервал на отрезки следующими точками и последовательно их исследовать.")
                extrema = [lower_bound]
                for _ in sorted(find_extrema(func, lower_bound, upper_bound)):
                    extrema.append(_)
                extrema.append(upper_bound)
                # print(extrema)

        for i in range(len(extrema)-1):
            lower_bound, upper_bound = extrema[i], extrema[i+1]
            print(f"Рассматриваемый отрезок [{lower_bound}; {upper_bound}]")
            check_convergence(deriv_func, lower_bound, upper_bound)
            if len(find_roots(func, lower_bound, upper_bound)) == 1:
                for method_name, method_func in methods:
                    root, iterations, val_at_root = method_func(func, lower_bound, upper_bound, epsilon, 10000, deriv_func)
                    roots.append(root)
                    print(f"\nМетод: {method_name}")
                    print(f"Root: {root}")
                    print(f"Iterations: {iterations}")
                    print(f"Value at the root: {round(val_at_root, 4)}")
                    print(f"Accuracy: {epsilon}")
                    print()
            else:
                print("На этом отрезке корней нет.")

        plot_function(func, extrema[0], extrema[-1], roots)
        exit()
    elif choice == 2:
        print("Выберите систему для вычисления:")
        print("1. x^2 - y^2 - 1 = 0; x + y - 3 = 0")
        print("2. x^2 + y^2 - 4 = 0; 3x^2 - y = 0")

        choice = input("Введите номер выбранной системы ")

        x0 = np.array([float(input("Введите начальные приближения для x: ")),
                       float(input("Введите начальные приближения для y: "))])

        x_values = np.linspace(-2, 2, 400)
        y_values = np.linspace(-2, 2, 400)
        X, Y = np.meshgrid(x_values, y_values)

        if choice == "1":
            result, num_iterations, errors = newton_method(system1, x0)
            Z1 = system1([X, Y])[0]
            Z2 = system1([X, Y])[1]
            plot_system(Z1, Z2, result)
        elif choice == "2":
            Z1 = system2([X, Y])[0]
            Z2 = system2([X, Y])[1]
            result, num_iterations, errors = newton_method(system2, x0)
            plot_system(Z1, Z2, result)
        print("Решение системы:", result)
        print("Количество итераций:", num_iterations)
        print("Вектор погрешностей:", errors)

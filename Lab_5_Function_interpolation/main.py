from functions import *

if __name__ == "__main__":

    # Выбор способа задания данных
    print("Выберите способ задания данных:")
    print("1. Ввод данных с клавиатуры")
    print("2. Загрузка данных из файла")
    print("3. Выбор функции")
    data_choice = int(input("Введите номер способа: "))

    if data_choice == 1:
        # Ввод данных с клавиатуры
        n = int(input("Введите количество узлов интерполяции: "))
        x = []
        y = []
        for i in range(n):
            x.append(float(input(f"Введите значение x_{i + 1}: ")))
            y.append(float(input(f"Введите значение y_{i + 1}: ")))
    elif data_choice == 2:
        # Загрузка данных из файла
        file_name = input("Введите имя файла: ")
        data = np.loadtxt(file_name)
        x = data[:, 0]
        y = data[:, 1]
    elif data_choice == 3:
        # Выбор функции
        print("Выберите функцию:")
        print("1. f(x) = x^2")
        print("2. f(x) = sin(x)")
        print("3. f(x) = exp(x)")
        function_choice = int(input("Введите номер функции: "))

        a = float(input("Введите начало интервала: "))
        b = float(input("Введите конец интервала: "))
        n = int(input("Введите количество узлов интерполяции: "))

        if function_choice == 1:
            x = np.linspace(a, b, n)
            y = x ** 2
        elif function_choice == 2:
            x = np.linspace(a, b, n)
            y = np.sin(x)
        elif function_choice == 3:
            x = np.linspace(a, b, n)
            y = np.exp(x)

    # Выбор метода интерполяции
    # print("Выберите метод интерполяции:")
    # print("1. Многочлен Лагранжа")
    # print("2. Многочлен Ньютона с разделенными разностями")
    # print("3. Многочлен Ньютона с конечными разностями")
    interpolation = InterpolationMethods(x, y)
    dd = interpolation.divided_differences()
    print("Таблица разделенных разностей:")
    print(dd)
    # Построение графиков
    plt.figure()
    plt.plot(x, y, 'o-', label="Исходная функция")

    # Построение графика многочлена Лагранжа
    x_interp = np.linspace(min(x), max(x), 100)
    y_interp = [interpolation.lagrange_polynomial(xi) for xi in x_interp]
    plt.plot(x_interp, y_interp, label="Многочлен Ньютона")

    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Интерполяция")
    plt.grid(True)

    # Вычисление приближенного значения функции
    x_value = float(input("Введите значение аргумента для вычисления: "))
    y_approx = interpolation.lagrange_polynomial(x_value)
    print(f"Приближенное значение функции (многочлен Лагранжа) для x = {x_value}: {y_approx}")
    y_approx = interpolation.newton_polynomial(x_value)
    print(f"Приближенное значение функции (многочлен Ньютона, разделенные разности) для x = {x_value}: {y_approx}")
    y_approx = interpolation.finite_diff_newton(x_value)
    print(f"Приближенное значение функции (многочлен Ньютона, конечные разности) для x = {x_value}: {y_approx}")
    plt.show()

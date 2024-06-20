import numpy as np
import matplotlib.pyplot as plt


class InterpolationMethods:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = len(x)

    def divided_differences(self):
        """
        Вычисляет таблицу разделенных разностей.

        Returns:
            Таблица разделенных разностей.
        """
        dd = np.zeros((self.n, self.n))
        dd[:, 0] = self.y
        for j in range(1, self.n):
            for i in range(self.n - j):
                dd[i, j] = float((dd[i + 1, j - 1] - dd[i, j - 1]) / (self.x[i + j] - self.x[i]))
        return dd

    def newton_polynomial(self, x_value):
        """
        Вычисляет значение многочлена Ньютона для заданного значения аргумента.

        Args:
            x_value: Значение аргумента.

        Returns:
            Значение многочлена Ньютона.
        """
        dd = self.divided_differences()
        y_value = self.y[0]
        term = 1
        for j in range(1, self.n):
            term *= (x_value - self.x[j - 1])
            y_value += dd[0, j] * term
        return y_value

    def lagrange_polynomial(self, x_value):
        """
        Вычисляет значение многочлена Лагранжа для заданного значения аргумента.

        Args:
            x_value: Значение аргумента.

        Returns:
            Значение многочлена Лагранжа.
        """
        y_value = 0
        for i in range(self.n):
            term = 1
            for j in range(self.n):
                if i != j:
                    term *= (x_value - self.x[j]) / (self.x[i] - self.x[j])
            y_value += self.y[i] * term
        return y_value

    # def finite_diff_newton(self, x):
    #     x_values = self.x
    #     y_values = self.y
    #     if x < x_values[0]:  # 1
    #         h = x_values[1] - x_values[0]
    #         f0 = y_values[0]
    #         df0 = (y_values[1] - y_values[0]) / h
    #
    #         result = f0 + df0 * (x - x_values[0])
    #     elif x > x_values[-1]:  # 2
    #         h = x_values[-1] - x_values[-2]
    #         fn = y_values[-1]
    #         dfn = (y_values[-1] - y_values[-2]) / h
    #
    #         result = fn + dfn * (x - x_values[-1])
    #     else:
    #         differences = [y_values]
    #
    #         for i in range(1, self.n):
    #             prev_diff = differences[i - 1]
    #             curr_diff = [(prev_diff[j + 1] - prev_diff[j]) for j in range(len(prev_diff) - 1)]
    #             differences.append(curr_diff)
    #
    #         h = x_values[1] - x_values[0]
    #         u = (x - x_values[0]) / h
    #
    #         result = y_values[0]
    #         for i in range(1, self.n):
    #             term = differences[i][0]
    #             for j in range(i):
    #                 term *= (u - j)
    #                 term /= (j + 1)
    #             result += term
    #
    #     return result
    def finite_diff_newton(self, x):
        x_values = self.x
        y_values = self.y

        if (x_values[0] < x < x_values[-1]):
            if x < (x_values[0] + x_values[-1]) / 2:  # Выбор первой формулы Ньютона
                differences = [y_values]
                for i in range(1, self.n):
                    prev_diff = differences[i - 1]
                    curr_diff = [(prev_diff[j + 1] - prev_diff[j]) for j in range(len(prev_diff) - 1)]
                    differences.append(curr_diff)

                h = x_values[1] - x_values[0]
                u = (x - x_values[0]) / h
                result = y_values[0]

                for i in range(1, self.n):
                    term = differences[i][0]
                    for j in range(i):
                        term *= (u - j)
                        term /= (j + 1)
                    result += term
            else:  # Выбор второй формулы Ньютона
                differences = [y_values[::-1]]
                for i in range(1, self.n):
                    prev_diff = differences[i - 1]
                    curr_diff = [(prev_diff[j] - prev_diff[j + 1]) for j in range(len(prev_diff) - 1)]
                    differences.append(curr_diff)

                h = x_values[-1] - x_values[-2]
                u = (x - x_values[-1]) / h
                result = y_values[-1]

                for i in range(1, self.n):
                    term = differences[i][0]
                    for j in range(i):
                        term *= (u + j)
                        term /= (j + 1)
                    result += term

        elif x < x_values[0]:
            h = x_values[1] - x_values[0]
            f0 = y_values[0]
            df0 = (y_values[1] - y_values[0]) / h

            result = f0 + df0 * (x - x_values[0])
        elif x > x_values[-1]:
            h = x_values[-1] - x_values[-2]
            fn = y_values[-1]
            dfn = (y_values[-1] - y_values[-2]) / h

            result = fn + dfn * (x - x_values[-1])

        # for i in range(0, len(x_values)):
        #     print(differences[i])
        # return result

    def c(self):
        return self.x

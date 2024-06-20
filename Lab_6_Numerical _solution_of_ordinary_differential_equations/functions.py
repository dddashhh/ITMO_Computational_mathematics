import numpy as np
import matplotlib.pyplot as plt


class ODE_Solver:
    def __init__(self, f, y0, x0, xn, h, e):
        self.f = f
        self.y0 = y0
        self.x0 = x0
        self.xn = xn
        self.h = h
        self.e = e

    def euler(self):
        x = np.arange(self.x0, self.xn + self.h, self.h)
        y = np.zeros_like(x)
        y[0] = self.y0
        for i in range(len(x) - 1):
            y[i + 1] = y[i] + self.h * self.f(x[i], y[i])
        return x, y

    def improved_euler(self):
        x = np.arange(self.x0, self.xn + self.h, self.h)
        y = np.zeros_like(x)
        y[0] = self.y0
        for i in range(len(x) - 1):
            y_star = y[i] + self.h * self.f(x[i], y[i])
            y[i + 1] = y[i] + self.h / 2 * (self.f(x[i], y[i]) + self.f(x[i + 1], y_star))
        return x, y

    def adams(self, n=10000):
        x = np.arange(self.x0, self.xn + self.h, self.h)
        y = np.zeros_like(x)
        y[0] = self.y0
        x_euler, y_euler = self.improved_euler()
        y[:n] = y_euler[:n]
        for i in range(n - 1, len(x) - 1):
            y[i + 1] = y[i] + self.h / 24 * (
                    55 * self.f(x[i], y[i]) - 59 * self.f(x[i - 1], y[i - 1]) + 37 * self.f(x[i - 2],
                                                                                            y[i - 2]) - 9 * self.f(
                x[i - 3], y[i - 3]))
        return x, y

    def runge_rule(self, x, y, p):
        x_half = np.arange(self.x0, self.xn + self.h / 2, self.h / 2)
        y_half = np.zeros_like(x_half)
        y_half[0] = self.y0
        for i in range(len(x_half) - 1):
            y_half[i + 1] = y_half[i] + self.h / 2 * self.f(x_half[i], y_half[i])
        return abs((y[-1] - y_half[-1]) / (2 ** p - 1))

    def accuracy_check(self, x, y, exact_solution):
        return max(abs(y - exact_solution(x)))


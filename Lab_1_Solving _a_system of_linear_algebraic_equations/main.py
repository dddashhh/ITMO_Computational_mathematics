from functions import *
import random


if __name__ == '__main__':
    A = []
    B = []
    command = input("Как задать матрицу? 1-Самостоятельно / 2-Из файла / 3-Задать случайно: ")

    if command == "1":
        n = int(input("Введите размерность матрицы: "))
        for i in range(n):
            A.append([float(j) for j in input(f"Введите коэффициенты при х в {i + 1} уравнении: ").split()])
        B = [int(i) for i in input("Введите строку со значениями уравнений: ").split()]

    elif command == "2":
        file_name = input("Введите путь до файла: ")
        with open(file_name, 'r') as file:
            n = int(file.readline())
            for i in range(n):
                A.append([float(num) for num in file.readline().split()])
            B = [float(num) for num in file.readline().split()]

    elif command == "3":
        n = int(input("Введите размерность матрицы: "))
        A = [[random.random() for i in range(3)] for j in range(3)]
        B = [random.random() for i in range(3)]

    x0 = np.array([10 for i in range(len(B))])
    tol = float(input("Введите точность: "))
    print("Исходная матрица:")
    for i in range(n):
        print(*A[i], B[i])
    res = simple_iteration(A, B, x0, tol)
    print(f"Вектор неизвестных: {res[0]}, количество итераций {res[1]+1}, погрешность {str(res[2])}")
    print("Решение найдено. Проверим наши вычисления, подставив вектор решения в исходную систему уравнений")

    print("Невязки: ")
    left_side = np.multiply(A, np.array([res[0] for i in range(n)]))
    for i in range(n):
        print(f"{sum(left_side[i])} ≈ {B[i]}")

import numpy as np


def rearrange_matrix(matrix_A, matrix_B):
    rows = len(matrix_A)
    new_matrix_A = [[0 for _ in range(rows)] for _ in range(rows)]
    new_matrix_B = [0 for _ in range(rows)]
    for i in range(rows):
        str_with_abs = [abs(h) for h in matrix_A[i]]
        k = str_with_abs.index(max(str_with_abs))
        new_matrix_A[k] = matrix_A[i]
        new_matrix_B[k] = matrix_B[i]
    return new_matrix_A, new_matrix_B


def isSquare(a):
    return all(len(row) == len(a) for row in a)


def simple_iteration(a, b, x0, tol=0.01, max_iter=1000):
    n = len(b)
    rows = len(a)
    x = x0.copy()
    # Если матрица не квадратная
    if isSquare(a) is False or [0 for _ in range(rows)] in a:
        exit("Матрица не квадратная")
    A = np.array(a)
    B = np.array(b)
    # Если размерность матриц не совпадает
    if rows != n:
        exit("Размерности матриц не совпадают")
    # Если определитель 0
    if np.linalg.det(A) == 0:
        exit("Определитель введенной матрицы А равен нулю")
    # Приведем матрицу к доминированию диагонали
    A = np.array(rearrange_matrix(a, b)[0])
    B = np.array(rearrange_matrix(a, b)[1])
    # Проверим достаточное условие сходимости итерационного процесса
    if [0.0 for j in range(rows)] in A:
        print("Условие преобладания диагональных элементов не выполнено")
        A = np.array(a)
    print("Преобразованная матрица:")
    for i in range(rows):
        print(*A[i])
    for k in range(max_iter):
        x_new = np.zeros(n)
        for i in range(n):
            s = np.dot(A[i], x)
            x_new[i] = x[i] + (B[i] - s) / A[i][i]
        print(f"Итерация {k+1} {[abs(x[i]-x_new[i]) for i in range(len(A))]}")
        if np.linalg.norm(x_new - x) < tol:
            return x_new, k, max([abs(x[i]-x_new[i]) for i in range(len(A))]), A, B
        x = x_new
    exit(f"Не удалось найти решение за {max_iter} итераций")

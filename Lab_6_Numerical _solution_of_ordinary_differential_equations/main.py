import matplotlib.pyplot as plt

from functions import *

if __name__ == "__main__":
    print("Выберите ОДУ:")
    print("1. y' = -y + 2*x")
    print("2. y' = (y^2 - x^2) / (y^2 + x^2)")
    print("3. y' = y - x^2 + 1")
    choice = int(input("Ваш выбор: "))

    # Define the ODE function
    if choice == 1:
        f = lambda x, y: -y + 2 * x
        exact_solution = lambda x: 2 * x - 2 + 2 * np.exp(-x)
    elif choice == 2:
        f = lambda x, y: (y ** 2 - x ** 2) / (y ** 2 + x ** 2)
        exact_solution = lambda x: x * np.tan(np.log(x))
    elif choice == 3:
        f = lambda x, y: y - x ** 2 + 1
        exact_solution = lambda x: x ** 2 + 2 * x + 1 + np.exp(x)
    else:
        exit("Неверный ввод.")

    # Get input from the user
    y0 = float(input("Введите начальное значение y0: "))
    x0 = float(input("Введите значение x0: "))
    xn = float(input("Введите значение xn: "))
    h = float(input("Введите размер шага: "))
    e = float(input("Введите требуемую точность: "))

    # Create an instance of ODE_Solver
    solver = ODE_Solver(f, y0, x0, xn, h, e)

    # Solve using different methods
    x_euler, y_euler = solver.euler()
    x_improved_euler, y_improved_euler = solver.improved_euler()
    x_adams, y_adams = solver.adams()

    # Calculate accuracy
    euler_accuracy = solver.runge_rule(x_euler, y_euler, 1)
    improved_euler_accuracy = solver.runge_rule(x_improved_euler, y_improved_euler, 2)
    adams_accuracy = solver.accuracy_check(x_adams, y_adams, exact_solution)

    # Print results
    print("Метод | x | y ")
    print("-" * 30)
    h_c = h
    while euler_accuracy > e:
        # print(f"Точность на данный момент: {euler_accuracy}, требуемая точность не достигнута, шаг h:{h_c}")
        h_c = h_c / 2
        solver = ODE_Solver(f, y0, x0, xn, h_c, e)
        x_euler, y_euler = solver.euler()
        euler_accuracy = solver.runge_rule(x_euler, y_euler, 1)
    for i in range(0, len(x_euler), int(h/h_c)):
        print(f"Euler | {x_euler[i]:.2f} | {y_euler[i]:.4f}")
    print(f" R = {euler_accuracy:.4f}, h = {h_c}, h_2 = {h_c / 2}")

    print("-" * 30)
    solver = ODE_Solver(f, y0, x0, xn, h, e)
    h_c = h
    while improved_euler_accuracy > e:
        h_c = h_c / 2
        solver = ODE_Solver(f, y0, x0, xn, h_c, e)
        x_improved_euler, y_improved_euler = solver.improved_euler()
        improved_euler_accuracy = solver.runge_rule(x_improved_euler, y_improved_euler, 2)
    for i in range(0, len(x_improved_euler), int(h/h_c)):
        print(f"Improved Euler | {x_improved_euler[i]:.2f} | {y_improved_euler[i]:.4f}")
    print(f" R = {improved_euler_accuracy:.4f} h = {h_c}, h_2 = {h_c / 2}")

    print("-" * 30)
    solver = ODE_Solver(f, y0, x0, xn, h_c, e)
    x_adams, y_adams = solver.adams()
    for i in range(0, len(x_adams), int(h/h_c)):
        print(f"Adams | {x_adams[i]:.2f} | {y_adams[i]:.4f} | {exact_solution(x_adams[i])}")
    print(f" R = {adams_accuracy:.4f}, h_c = {h_c}, h_2 = {h_c / 2}")


    # Plot results
    plt.plot(x_euler, y_euler, label="Euler")
    plt.plot(x_improved_euler, y_improved_euler, label="Improved Euler")
    plt.plot(x_adams, y_adams, label="Adams")
    plt.plot(x_euler, exact_solution(x_euler), label="Exact Solution")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()

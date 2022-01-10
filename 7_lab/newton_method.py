import matplotlib.pyplot as plt

from functions import fun_with_param, derivative_fun_with_param, fun, derivative_fun


def newton_method_with_param(x, n, a, b, eps, number):
    root = x
    N = 0
    for i in range(n):
        N += 1
        root = x - (fun_with_param(a, b, x) /
                    derivative_fun_with_param(a, b, x))
        if abs(root - x) < eps:
            break
        x = root
    print("Метод Ньютона X: ", round(root, number), ' за ', N, 'итераций')
    y = fun_with_param(a, b, root)
    plt.scatter(root, y, color="red")


def newton_method_without_param(x, n, eps, number):
    root = x
    N = 0
    for i in range(n):
        N += 1
        root = x - (fun(x) / derivative_fun(x))
        if abs(root - x) < eps:
            break
        x = root
    print("Число итераций: ", N)
    print("Без параметров: ", round(root, number))

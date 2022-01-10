import matplotlib.pyplot as plt
import numpy as np

from functions import fun_with_param, fun


def hord_method_with_params(x0, iterations, a, b, eps, round_to, intervalA, intervalB):
    x = intervalA
    x_prev = x + 2 * eps
    i = 0

    while np.abs(x - x_prev) >= eps:
        x_prev = x
        #первый вариант 15 формулы из методички, выбор зависит от графика функции
        x = x - (intervalB - x)*fun_with_param(a, b, x) / \
            (fun_with_param(a, b, intervalB) - fun_with_param(a, b, x))
        i += 1

    print("Метод хорд. X: ", round(x, round_to), ' за ', i, 'итераций')
    y = fun_with_param(a, b, x)
    plt.scatter(x, y, color="red")


def hord_method_without_params(x0, iterations, eps, round_to, intervalA, intervalB):
    x = intervalA
    x_prev = x0 + 2 * eps
    i = 0

    while np.abs(x - x_prev) >= eps or i < iterations:
        x_prev = x
        x = x - (intervalB - x)*fun(x)/(fun(intervalB) - fun(x))
        i += 1
    print("Число итераций: ", i)
    print("Без параметров: ", round(x, round_to))

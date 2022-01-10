import matplotlib.pyplot as plt
import numpy as np

from dichotomy_method import dichotomy_method_without_param
from functions import fun_with_param, fun
from hord_method import hord_method_without_params
from newton_method import newton_method_without_param
from iteration_method import iteration_method_without_param


def create_plot(x, y1, y2, title):
    plt.title(title)
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.grid(True)
    plt.show()


# Вводим начальные значения
#a = float(input("Параметр a: "))
#b = float(input("Параметр b: "))
c = 1
d = 1

x = np.linspace(-10, 10, 1000)

y1 = fun(x)
#y2 = fun(x)

plt.plot(x, y1)
plt.plot(x, [0 for x in x])
plt.grid(True)
plt.show()

# intervalA = float(input("Левая граница: "))
# intervalB = float(input("Правая граница: "))


x0 = float(input("Начальное приближение x: "))
eps = 0.001

s = str(eps)
number = abs(s.find('.') - len(s)) - 1

n = int(input("Число итераций n: "))


#print("Метод простых итераций")

iteration_method_without_param(x0, eps, number)

create_plot(x, y1, [0 for x in x], "Метод простых итераций")

# print("Метод Ньютона")

# newton_method_without_param(x0, n, eps, number)

# create_plot(x, y1, [0 for x in x], "Метод Ньютона")

# print("Метод дихотомии")

# dichotomy_method_without_param(eps, number, intervalA, intervalB)

# create_plot(x, y1, [0 for x in x], "Метод дихотомии")


# hord_method_without_params(x0, n, eps, number, intervalA, intervalB)

# create_plot(x, y1, [0 for x in x], "Метод хорд")

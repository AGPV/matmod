import numpy as np
import matplotlib.pyplot as plt
from gold import gold
from fib import fib
from function import function
def draw():
  x = np.linspace(-100, 100, 1000)
  plt.plot(x, function(x))
  plt.grid(True)
  plt.show()




draw()
a = float(input("Введите a: "))
b = float(input("Введите b: "))
e = float(input("Введите точность при нахождении экстремума: "))
n = int(input("Введите n: "))
ver = int(input("0 - Золотое сечение | 1 - Фибоначи \n"))
if (ver == 0):
    extrx, n = gold(a, b, e)
else:
    extrx = fib(a, b, n)
extry = function(extrx)
print('Число итераций: ', n)
print('x: ', extrx, 'y: ', extry)

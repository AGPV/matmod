import warnings
import numpy as np
import random
from numpy.ma.core import maximum
import matplotlib.pyplot as plt
from hack import MonteKar1o
from scipy import integrate
def draw():
  f, a, b = function()
  fig = plt.subplots()
  x = np.linspace(a, b, 100)
  plt.plot(x, f(x))
  plt.grid(True)
  plt.show()

def function():
  return lambda x: x**2, 0.3, 3

def get_M(a, b, f): #ищем максимум и минимум функции
    val = []
    for x in np.linspace(a, b, 1000):
        val.append(f(x))

    return max(val), min(val)

def generate_random_variables(x): 
  return [random.random() for _ in range(x)]

class Integrator:
  @staticmethod
  def analytically():
    f, a, b = function()
    return np.abs(integrate.quad(f, a, b)[0]) # аналитический интеграл по Ньютона-Лейбница

  @staticmethod
  def trapezium(): # n - число трапеций
    n = 32
    f, a, b = function()
    I = 0
    while (np.abs(I - ian)>ian*0.01):
      n *= 2
      h = (b - a) / n
      while round(a, 8) < b:
        I += 0.5 * h * (f(a) + f(a + h))
        a += h
    return I, n

ian = Integrator.analytically()

class MonteKarlo: 
  @staticmethod
  def first():
    N = 1
    I = 0
    f, a, b = function()
    while (np.abs(I - ian)>ian*0.01):
      N *= 2
      sum = 0
      random_values = generate_random_variables(N) #получаем набор N базовыхъ чисел на интервале (0, 1)
      for i in range(N):
        u =  random_values[i] * (b - a) + a #по методу обратных функций получаем значения u равномерно распределённые на интервале [a, b]
        sum += f(u) #для каждой точки выполняем функциональное преобразование
      I = ((b - a) / N) * sum # умножаем длину отрезка ab на матожидание
    return  I, N

  @staticmethod
  def second():
    I = 0
    n = 128
    f, a, b = function()
    maxmimum, minimimum = get_M(a, b, f)
    while (np.abs(I - ian)>ian*0.01):
      k = 0
      n *= 2
      for _ in range(n):
        x = a + ((b - a) * random.random()) #случайная величина от a до b
        y =  minimimum + ((maxmimum - minimimum) * random.random()) #случайная величина от minimum до maximum
        if y < f(x):
          k += 1    #Считаем количество точек, попавших под кривую
      I = (maxmimum - minimimum) * (b - a) * (k/n)  #умножаем площадь прямоугольника на (k/n)
    return I, n




draw()
print('Аналитическое выражение: ', Integrator.analytically())
ti, tn = Integrator.trapezium()
print('Метод трапеций: ', ti, ' за ', tn, ' узлов')
fi, fn = MonteKarlo.first()
print('Первый метод Монте-Карло: ', fi, ' за ', fn, ' узлов')
si, sn = MonteKar1o.second()
print('Второй метод Монте-Карло: ', si, ' за ', sn, ' узлов')
print('Выборочные среднеквадратичные отклонения для первого', np.std([MonteKarlo.first()[0] for _ in range(100)]))
print('Выборочные среднеквадратичные отклонения для второго', np.std([MonteKar1o.second()[0] for _ in range(100)]))

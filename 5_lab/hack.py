import numpy as np
from scipy import integrate
import random

def function():
  return lambda x: x**2, 0.3, 3

class Integrator:
  @staticmethod
  def analytically():
    f, a, b = function()
    return np.abs(integrate.quad(f, a, b)[0]) # аналитический интеграл по Ньютона-Лейбница

  @staticmethod
  def trapezium(n = 128): # n - число трапеций
    f, a, b = function()
    h = (b - a) / n # высота
    s = 0
    while round(a, 8) < b:
      s += 0.5 * h * (f(a) + f(a + h)) # считаем площадь
      a += h # сдвигаем левый край
    return np.abs(s)


class MonteKar1o: 
  @staticmethod
  def second():
    ian = Integrator.analytically()
    N = 1024
    I = 0
    f, a, b = function()
    while (np.abs(I - ian)>ian*0.01):
      N *= 2
      sum = 0
      random_values = [random.random() for _ in range(N)] #получаем набор N базовыхъ чисел на интервале (0, 1)
      for i in range(N):
        u =  random_values[i] * (b - a) + a #по методу обратных функций получаем значения u равномерно распределённые на интервале [a, b]
        sum += f(u) #для каждой точки выполняем функциональное преобразование
      I = ((b - a) / N) * sum #формула 10 из методички
    return  I, N
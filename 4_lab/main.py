import matplotlib.pyplot as plt
import gaus
import revfrasp
import rel
from histogram import *

n = int(input("Введите N: "))
a = float(input("Введите a: "))
b = float(input("Введите b: "))
mw = float(input("Введите математическое ожидание: "))
disp = float(input("Введите квадрат дисперсии: "))
sig = float(input("Введите параметр распределения для релеевской случ. вел.: "))
print("1 - метод обратных функций | 2 - по гауссовскому закону | 3 - метод Неймана")
ver = int(input("Введите, для какой выборки построить: "))



histandnpol(ver, a, b, n, mw, disp, sig)
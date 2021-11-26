import matplotlib.pyplot as plt
from histogram import *
from calc import *

n = int(input("Введите N: "))
a = float(input("Введите a: "))
b = float(input("Введите b: "))
mw = float(input("Введите математическое ожидание: "))
disp = float(input("Введите квадрат дисперсии: "))
sig = float(input("Введите параметр распределения для релеевской случ. вел.: "))

print("1 - метод обратных функций | 2 - по гауссовскому закону | 3 - метод Неймана")
ver = int(input("Введите, для какой выборки построить: "))

input("Гистограмма")
histdraw(ver, a, b, n, mw, disp, sig)

input("Полигон")
x = polydraw(ver, a, b, n, mw, disp, sig)

if (ver == 1):
    printcalcf(x)
elif (ver == 2):
    printcalcs(x, mw, disp)
elif (ver == 3):
    printcalct(x, b)


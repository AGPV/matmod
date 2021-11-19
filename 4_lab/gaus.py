import numpy as np
import random as rnd

#Сформировать выборку величин, распределенных по гауссовскому закону с параметрами 𝑁(𝑚𝑥, 𝜎𝑥^2) на основе ЦПТ
#Закон гаусовского распределения 
def gauss(mw, disp): #(мат. ожидание, дисперсия)
    disp = np.sqrt(disp)
    n = 6            #число членов суммы
    v = 0            #сумма (ri - 0.5)
    x = []
    for i in range(10):
        v = 0
        for j in range(n):
            v += rnd.random()-0.5
        eps = np.sqrt(12/n)*v       #[15 формула из методички]
        res = disp * eps + mw
        x.append(res)
    return x

mw = float(input("Введите математическое ожидание: "))
disp = float(input("Введите квадрат дисперсии: "))

print(gauss(mw,disp))
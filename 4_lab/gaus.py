import numpy as np
import random as rnd

#Сформировать выборку величин, распределенных по гауссовскому закону с параметрами 𝑁(𝑚𝑥, 𝜎𝑥^2) на основе ЦПТ
#Закон гаусовского распределения 
def gauss(mw, disp, count): #(мат. ожидание, дисперсия)
    disp = np.sqrt(disp)
    n = 6            #число членов суммы
    x = []
    for i in range(count):
        v = 0
        for j in range(n):
            v += rnd.random()-0.5
        res = gausraspr(n, v, mw, disp)
        x.append(res)
    return x

def gausraspr(n, v, mw, disp): #[15 формула из методички]
    eps = np.sqrt(12/n)*v
    res = disp * eps + mw
    return res
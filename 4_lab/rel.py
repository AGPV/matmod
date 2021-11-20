import numpy as np
import random as rnd

#ЛЮТОЕ ОБЪЯСНЕНИЕ В ПАИНТЕ
#Probability density/плотность распределения
def probden(x, b):
    return (x / (b ** 2)) * np.exp(-1 * ((x ** 2) / (2 * (b ** 2))))    #[11 формула в методичке]

def reley(a, b, n, sig):
    res = []
    m = probden(sig,sig)    #верхняя граница

    #disp = (2 - np.pi/2)*(b**2)     #дисперсия
    i = 0
    while i < n:
        x = a + ((b-a) * rnd.random())
        y = m * rnd.random()         #[Две формулы из Алгоримта метода Неймана. (стр.11 п.2)]
        if y < probden(x,sig):
            res.append(x)
            i += 1
    return res
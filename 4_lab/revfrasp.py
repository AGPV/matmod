import numpy as np
import random as rnd

#Сформировать выборку непрерывных равно распределенных на интервале (𝑎, 𝑏) случайных величин методом обратных функций.

#Обратная функция распределения случ вел равномерной X на (a, b) [10 формула в методичке] 
def revraspr(x, a, b):
    return x*(b-a)+a

def revmetod(a, b, n):
    #выборка независимых значений r
    r = np.array([rnd.random() for i in range(n)])
    x = []
    for i in r:
        temp = revraspr(i, a, b)
        x.append(temp)
    return x

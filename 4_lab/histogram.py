import matplotlib.pyplot as plt
from revfrasp import *
import numpy as np
from gaus import *
from rel import *

#[16 формула из методички]
def fgauss(mw, disp, x):
    ch = np.exp(-1*((x - mw)**2)/(2*disp**2))
    zn = np.sqrt(2*np.pi*(disp**2))
    return ch/zn

#[11 формула из методички]
def freley(sig, x):
    return (x / (sig ** 2)) * np.exp(-1 * ((x ** 2) / (2 * (sig ** 2))))


#[7 формула из методички]
def frevmetod(a, b, x):
    if a <= x <= b:
        return (x - a) / (b - a)
    elif x >= b:
        return 1
    else:
        return 0


def histo(x):
    N = len(x)
    newx = sorted(x)
    min = newx[0]                 #могу себе позволить, т.к. list отсортирован
    max = newx[len(newx)-1]       #поправочный множитель = 0
    d = max - min
    k = 4 * np.log10(N)
    delta = d/k
    bord = []                     #list с границами интервалов
    kbord = [0]                #list с количеством элементов попавших в iтый интервал
    i = 1
    while i <= k:
        bord.append((min + (i - 1) * delta, min + i * delta))
        i += 1
    i = 0
    for check in newx:              #работает, но где-то погрешность, всегда одинаковая для одинаковых k
        if check <= bord[i][1]:
            kbord[i] += 1
        else:
            i += 1
            kbord.append(1)
    freq = []
    i = 0
    while i <= len(kbord)-1:
        freq.append(kbord[i]/N)
        i += 1

    return newx, freq

def histandnpol(ver, a, b, n, mw, disp, sig):
    r=[]
    if ver == 1:
        test, y = histo(revmetod(a, b, n))
        for temp in test:
            r.append(frevmetod(a, b, temp))

    elif ver == 2:
        test, y = histo(gauss(mw, disp, n))
        for temp in test:
            r.append(fgauss(mw, disp, temp))

    elif ver == 3:
        test, y = histo(reley(a, b, n, sig))
        for temp in test:
            r.append(freley(sig, temp))
    else: 
        return print("WRONG version")
    fig, ax = plt.subplots()
    x = range(len(y))
    ax.bar(x, y)
    plt.plot(test, r)
    plt.show()
import matplotlib.pyplot as plt
import numpy as np
from revfrasp import *
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
        return 1 / (b - a)
    else:
        return 0


def histo(x):
    N = len(x)
    newx = sorted(x)
    a = newx[0]                 #могу себе позволить, т.к. list отсортирован
    b = newx[len(newx)-1]       #поправочный множитель = 0
    d = b - a
    k = 3 * np.log10(N)
    delta = d/k
    bord = []                     #list с границами интервалов
    kbord = [0]                #list с количеством элементов попавших в iтый интервал
    i = 1
    while i <= k:
        bord.append((a + (i - 1) * delta, a + i * delta))
        i += 1
    i = 0
    for check in newx:
        if check <= bord[i][1]:
            kbord[i] += 1
        else:
            i += 1
            kbord.append(1)
    freq = []
    midx = []
    i = 0
    while i <= len(kbord)-1:
        freq.append(kbord[i]/(N))
        
        midx.append((bord[i-1][0]+bord[i-1][1])/2)   #криво сломал и криво починил, на 12 час кодинга адекватного решения не вижу, не понимаю в чём ошибка и как я её решил
        i += 1

    return newx, freq, midx
    #return freq


def poly(x):
    N = len(x)
    newx = sorted(x)
    a = newx[0]                 #могу себе позволить, т.к. list отсортирован
    b = newx[len(newx)-1]       #поправочный множитель = 0
    d = b - a
    k = 3 * np.log10(N)
    delta = d/k
    bord = []                     #list с границами интервалов
    kq = [0]                #list с количеством элементов попавших в iтый интервал
    q = 1
    while q <= k:
        bord.append((a, a + q * delta))
        q += 1
    i = 0
    for check in newx:
        if check <= bord[i][1]:
            kq[i] += 1
        else:
            i += 1
            kq.append(1)
    
    q = 1
    freqx = [a]
    while q <= k:
        freqx.append(a + q * delta)
        q += 1

    q = 0
    freqy = []
    while q <= k:
        freqy.append(kq[q-1]/N)
        q += 1
    
    return freqx, freqy



def histdraw(ver, a, b, n, mw, disp, sig):
    r=[]
    if ver == 1:
        newx, y, midx = histo(revmetod(a, b, n))
        for temp in newx:
            r.append(frevmetod(a, b, temp))

    elif ver == 2:
        newx, y, midx = histo(gauss(mw, disp, n))
        for temp in newx:
            r.append(fgauss(mw, disp, temp))

    elif ver == 3:
        newx, y, midx = histo(reley(a, b, n, sig))
        for temp in newx:
            r.append(freley(sig, temp))
    else: 
        return print("WRONG version")
    fig, ax = plt.subplots()
    x = midx
    
    ax.grid()
    ax.bar(x, y)
    plt.plot(newx, r)
    plt.show()
    return y

def polydraw(ver, a, b, n, mw, disp, sig):
    r=[]
    if ver == 1:
        x, y = poly(revmetod(a, b, n))
        for temp in x:
            r.append(frevmetod(a, b, temp))

    elif ver == 2:
        x, y = poly(gauss(mw, disp, n))
        for temp in x:
            r.append(fgauss(mw, disp, temp))

    elif ver == 3:
        x, y = poly(reley(a, b, n, sig))
        for temp in x:
            r.append(freley(sig, temp))
    else: 
        return print("WRONG version")
    fig, ax = plt.subplots()
    ax.step(x, y, "g-o", where= 'post')          #'pre', 'post', 'mid'
    ax.grid()
    plt.plot(x, r)
    plt.show()
    return y
#print(histo(gauss(0, 2, 1000)))
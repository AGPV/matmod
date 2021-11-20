import numpy as np
from gaus import *
from rel import *
from revfrasp import *

#Первый выборочный момент
def fmom(x):
    res = 0
    for i in x:
        res += i
    return res/len(x)

#Второй выборочный момент с известным средним
def smom(x, m):
    res = 0
    for i in x:
        res += (i-m)**2
    return res

#Второй выборочный момент  при неизвестном заранее среднем
def smomunknwn(x):
    res = 0
    for i in x:
        res += (i-fmom(x))**2
    return res

def printcalcf(x):
    a = x[0]
    b = x[len(x)-1]
    m1 = fmom(x)
    m2 = (b+a)/2
    d1 = smomunknwn(x)
    d2 = ((b-a)**2)/12
    print("Первый выборочный момент = ",m1)
    print("Математическое ожидание = ", m2)
    print("Абсолютная погрешность = ", np.abs(m1-m2))
    print("Относительная погрешность = ", (np.abs(m1-m2)/m2)*100, "%")


    print("Второй выборочный момент = ",d1)
    print("Дисперсия = ", d2)
    print("Абсолютная погрешность = ", np.abs(d1-d2))
    print("Относительная погрешность = ", (np.abs(d1-d2)/d2)*100, "%") 


def printcalcs(x, m2, d2):
    m1 = fmom(x)
    d1 = smomunknwn(x)
    print("Первый выборочный момент = ",m1)
    print("Математическое ожидание = ", m2)
    print("Абсолютная погрешность = ", np.abs(m1-m2))
    print("Относительная погрешность = ", (np.abs(m1-m2)/m2)*100, "%")


    print("Второй выборочный момент = ",d1)
    print("Дисперсия = ", d2)
    print("Абсолютная погрешность = ", np.abs(d1-d2))
    print("Относительная погрешность = ", (np.abs(d1-d2)/d2)*100, "%") 

def printcalct(x, b):
    m1 = fmom(x)
    m2 = np.sqrt(np.pi*(b**2)/2)
    d1 = smomunknwn(x)
    d2 = ((2 - np.pi/2)*(b**2))
    print("Первый выборочный момент = ",m1)
    print("Математическое ожидание = ", np.sqrt(np.pi*(b**2)/2))
    print("Абсолютная погрешность = ", np.abs(m1-m2))
    print("Относительная погрешность = ", (np.abs(m1-m2)/m2)*100, "%")


    print("Второй выборочный момент = ",d1)
    print("Дисперсия = ", d2)
    print("Абсолютная погрешность = ", np.abs(d1-d2))
    print("Относительная погрешность = ", (np.abs(d1-d2)/d2)*100, "%") 
import numpy as np
import matplotlib.pyplot as plt

def draw():
  x = np.linspace(-100, 100, 1000)
  plt.plot(x, function(x))
  plt.grid(True)
  plt.show()

def function(x):
  return (x**2)*np.sin(x)

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

#draw()
a = float(input("Введите a: "))
b = float(input("Введите b: "))
e = float(input("Введите e: "))
n = int(input("Введите n: "))

print('Число итераций: ', n)

while(((b-a)/fibonacci(n)) > e):
  n+=1


xl = a + ((fibonacci(n-2)/fibonacci(n))*(b-a))
xr = a + ((fibonacci(n-1)/fibonacci(n))*(b-a))
yl = function(xl)
yr = function(xr)

print(n)
while(n != 1):
    n = n-1
    if (yl < yr):
        a = xl
        xl = xr
        xr = b - (xl -a)
        yl = yr
        yr = function(xr)
    else:
        b = xr
        xr = xl
        xl = a + (b - xr)
        yr = yl
        yl = function(xl)

extrx = ((xl+xr)/2)
extry = function(extrx)
print('x: ', extrx, 'y: ', extry)
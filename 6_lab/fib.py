import numpy as np
from function import function

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def fib(a, b, n):
    xl = a + ((fibonacci(n-2)/fibonacci(n))*(b-a))
    xr = a + ((fibonacci(n-1)/fibonacci(n))*(b-a))
    yl = function(xl)
    yr = function(xr)
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
    return (xl+xr)/2
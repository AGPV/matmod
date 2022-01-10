import numpy as np


def fun_with_param(a, b, x):
    return np.tan(x - a) - (b*x)


def phi_with_param(a, b, x):
    # x - f(x)/f'(x)
    return x - fun_with_param(a, b, x)/derivative_fun_with_param(a, b, x)


def derivative_fun_with_param(a, b, x):
    return -b + 1/(np.cos(x-a)**2)


def derivative_phi_with_param(a, b, x):
    # не исправлял
    return a/(b*np.cos(a*x/b)**2)


def fun(x):
    return x ** 2 - 4*x


def phi(x):
    return np.sqrt(4*x)


def derivative_fun(x):
    return 4*x-4


def derivative_phi(x):
    return 1/np.sqrt(x)

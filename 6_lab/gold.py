from function import function


def gold(a, b, e):
    FI = 1.618

    x1 = b - ((b-a)/FI)
    x2 = a + ((b-a)/FI)

    n = 0
    while((b-a)/2 >= e):
        n += 1
        yl = function(x1)
        yr = function(x2)
        if yl < yr:
            a = x1
            x1 = x2
            x2 = b - (x1 - a)
        elif yl > yr:
            b = x2
            x2 = x1
            x1 = a + (b - x2)
    return (a+b)/2, n

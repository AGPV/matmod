import matplotlib.pyplot as plt
import numpy as np
import json

# Считает сумму xk в степени v по k
def sumk(x, v):
    z = 0
    for i in range(len(x)):
        z = z + (x[i]**v)
    return z

# Считает сумму yk*(xk в степени v) по к
def sumres(x,y,v):
    z = 0
    for i in range(len(x)):
        z = z + (y[i]*(x[i]**v))
    return z


def appr(x, y, gr):  
    fp = np.polyfit(x, y, gr, full=True)[0]
    f = np.poly1d(fp)
    fx = np.linspace(np.min(x), np.max(x), 1000)
    plt.plot(fx, f(fx))
    plt.grid(True)
    return f
#
def sq(x, y, gr):  
    coef = np.zeros((gr, gr)) # Матрица коэффициентов при неизвестных
    free = np.zeros(gr) # Вектор свободных членов

    # Сортировка пузырьком
    for i in range(len(x)):
        for j in range(len(x)-i-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
                y[j], y[j+1] = y[j+1], y[j]
    
    for i in range(gr):
        for j in range(gr):
            coef[i][j] = sumk(x, i+j)
        free[i] = sumres(x, y, i)
    coef[0][0] = 1
    return np.linalg.solve(coef, free)

def pol(c, t):
    z = 0
    for i in range(len(x)-1):
        z = z + c[i]*(t**i)
    return z

# Открываем json файл.      Тест — './data.json'
with open('data.json', 'r') as f:
    data = json.load(f)

grade = int(input("Введите степень аппроксимирующего полинома: "))

# Записываем, какие номера нам нужно выводить
shown = list(
    input("Введите номера графиков: ").split())

# Записываем данные из json в массив
for label in data:
    data[label]["x"] = list(map(float, data[label]["x"].split()))
    data[label]["y"] = list(map(float, data[label]["y"].split()))

# Выкидываем ненужные графики
res = list(data.items())
i = 0
while i < len(res):
    if res[i][0] not in shown:
        res.pop(i)
        i -= 1
    i += 1

leg = []
for label, coord in res:
    x = np.array(coord["x"], dtype=float)
    y = np.array(coord["y"], dtype=float)
    plt.scatter(x, y)
    #xnew = np.linspace(np.min(x), np.max(x), 1000)
    #ynew = appr(x,y,grade)
    appr(x,y,grade)
    leg = leg + list(label)
plt.legend(leg, loc='best')
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
import json


def partparab(x, y, t):  # Принимает np массивы с координатами точек и значение x, для которого будет считать
    z = 0
    for i in range(len(x)-1):
        if t >= x[i] and t <= x[i+1]:
            # Решаем систему уравнений через матрицу
            M = np.array(
                [[x[i-1]**2, x[i-1], 1], [x[i]**2, x[i], 1], [x[i+1]**2, x[i+1], 1]])
            v = np.array([y[i-1], y[i], y[i+1]])
            solve = np.linalg.solve(M, v)  # [a, b, c]
            z = solve[0]*t**2 + solve[1]*t + solve[2]
        i += 1
    return z


# Открываем json файл.      Тест — './data.json'
with open(input("Enter file path: "), 'r') as f:
    data = json.load(f)

# Записываем, какие номера нам нужно выводить
shown = list(
    input("Enter the numbers of the graphs you want to show: ").split())

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
    xnew = np.linspace(np.min(x), np.max(x), 100)
    ynew = [partparab(x, y, i) for i in xnew]
    plt.plot(xnew, ynew)
    leg = leg + list(label)
plt.legend(leg, loc='best')
plt.grid(True)

plt.show()

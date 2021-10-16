import matplotlib.pyplot as plt
import numpy as np
import json


def partline(x, y, t):  # Принимает np массивы с координатами точек и значение x, для которого будет считать
    z = 0
    # Сортировка пузырьком
    for i in range(len(x)):
        for j in range(len(x)-i-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]  
                y[j], y[j+1] = y[j+1], y[j]  

    for i in range(len(x)-1):
        if t >= x[i] and t <= x[i+1]:
            z = y[i] + (y[i+1]-y[i])*(t-x[i])/(x[i+1]-x[i])
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
    ynew = [partline(x, y, i) for i in xnew]
    plt.plot(xnew, ynew)
    leg = leg + list(label)

plt.legend(leg, loc='best')
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import json

#Открываем json файл.      Тест — './data.json'
with open(input("Enter file path: "), 'r') as f:   
    data = json.load(f)

#Записываем, какие номера нам нужно выводить
shown = list(input("Enter the numbers of the graphs you want to show: ").split())

#Записываем данные из json в массив
for label in data: 
    data[label]["x"] = list(map(float, data[label]["x"].split()))
    data[label]["y"] = list(map(float, data[label]["y"].split()))

#Выкидываем ненужные графики
res = list(data.items())
i = 0
while i < len(res):
    if res[i][0] not in shown:
        res.pop(i)
        i -= 1
    i += 1

#Переносим точки на plot 
for label, coord in res:
    plt.scatter(coord["x"], coord["y"])

plt.show()
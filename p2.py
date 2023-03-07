import matplotlib.pyplot as plt
import numpy as np
# Відкриття файлу з вхідними даними
with open('input.txt', 'r') as f:
    data = [float(line.strip()) for line in f.readlines()]

# Отримання значення вікна осереднення від користувача або з файлу
window_size = input("Введіть розмір вікна осереднення або залиште порожнім, щоб використати значення з файлу: ")
if window_size.strip() == "":
    with open('window_size.txt', 'r') as f:
        window_size = int(f.readline().strip())
else:
    window_size = int(window_size)

# Операція осереднення
averages = []
for i in range(len(data)):
    window = data[max(0, i - window_size + 1):i + 1]
    average = sum(window) / len(window)
    averages.append(average)

# Запис результатів в файл та виведення їх на екран
with open('output.txt', 'w') as f:
    for i in range(len(data)):
        diff = averages[i] - data[i]
        f.write(f"{i+1} - {data[i]} - {averages[i]} - {diff}\n")
        print(f"{i+1} - {data[i]} - {averages[i]} - {diff}")

# Відображення графіку
plt.plot(range(len(data)), data, label="Вхідні дані")
plt.plot(range(len(averages)), averages, label="Осереднені дані")
plt.xlabel("Номер числа")
plt.ylabel("Значення")
plt.legend()
plt.show()

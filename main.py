import math
import numpy as np
import matplotlib.pyplot as plt

accVol = 50  # (Вольт) ускоряющиеся напряжение
width = 0.55 * (10**-9)  # (Метры) ширина щели
h = 1.054571817 * (10 ** -34)  # (Дж * с) постоянно планка
PI = math.pi # число Пи
m = 9.1093837 * (10 ** -31) # (кг) масса электрона
e = 1.60217663 * (10 ** -19) # Кулона заряд электрона
measurements = int(input()) # Количество измерений

if width > 10 ** -9 :
    raise Exception("Opening is too wide")

def pxk(k):
    return ((2 * k - 1) * PI) / 12

p = (e * accVol * 2 * m) ** 0.5 # (кг * м) / c, импульс p частицы

def wave(px):
    return np.sqrt(width / (2 * PI * h)) * np.sin(px * width / (2 * h)) / (px * width / (2 * h))

def mod_wave(px):
    return np.square(np.abs(wave(px)))

def phi_k(pxk):
    return math.asin(pxk / p)


max = mod_wave(pxk(1))
sum = 0
expected = []
for i in range(1, 11):
    t = mod_wave(pxk(i)) / max
    expected.append(t)
    sum += t
print(expected)
borders = [0]
for i in range(0, len(expected)):
    borders.append(borders[i] + expected[i] / sum)
print(borders)

sensors = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0, measurements):
    rand = np.random.random()
    for j in range(0, len(expected)):
        if rand < borders[j + 1]:
            sensors[j] += 1
            break
print(sensors)

norm = []
for i in range(0, len(sensors)):
    norm.append(sensors[i] / sensors[0])
print(norm)
print("Длина волны де Бройля")
print(h/p)

plt.bar(range(0, len(norm)), norm)
plt.bar(range(0, len(expected)), expected, fill=False, hatch='/')
plt.xticks(np.arange(0, 10, step=1))
plt.show()
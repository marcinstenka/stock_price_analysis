import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

csv = pd.read_csv("dane.csv")
data = csv['Najwyzszy'].to_numpy()

EMA12 = np.zeros(1009)
N12 = 12
alfa_N12 = 2/(N12+1)

EMA26 = np.zeros(1009)
N26 = 26
alfa_N26 = 2/(N26+1)

SIGNAL = np.zeros(1000)
N9 = 9
alfa_N9 = 2/(N9+1)


for i in range(0,1009):
    for n in range(0, N12 + 1):
        temp_mianownik=0
        temp_licznik=0
        if n == N12:
            temp_licznik += data[i + n]
            temp_mianownik += 1
            EMA12[i] = temp_licznik/temp_mianownik
            break
        temp_licznik += data[i + n] * pow((1 - alfa_N12), n)
        temp_mianownik += pow((1-alfa_N12), n)

for i in range(0,1009):
    temp_mianownik=0
    temp_licznik=0
    for n in range(0, N26 + 1):
        if n == N26:
            temp_licznik += data[i + n]
            temp_mianownik += 1
            EMA26[i] = temp_licznik/temp_mianownik
            break
        temp_licznik += data[i + n] * pow((1 - alfa_N26), n)
        temp_mianownik += pow((1-alfa_N26), n)


MACD = EMA12-EMA26

for i in range(0,1000):
    temp_mianownik=0
    temp_licznik=0
    for n in range(0, N9 + 1):
        if n == N9:
            temp_licznik += MACD[i + n]
            temp_mianownik += 1
            SIGNAL[i] = temp_licznik/temp_mianownik
            break
        temp_licznik += MACD[i + n] * pow((1 - alfa_N9), n)
        temp_mianownik += pow((1-alfa_N9), n)

fig, axs = plt.subplots(2)
axs[0].plot(data)
axs[1].plot(MACD)
axs[1].plot(SIGNAL)

plt.show()


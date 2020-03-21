""" Movimento Uniformemente Variado """

import matplotlib.pyplot as plt
import numpy as np

so = float(input("Digite a posição inicial: "))
vo = float(input("Digite a velocidade inicial: "))
a = float(input("Digite a aceleração: "))

space = np.zeros(shape=10, dtype=float, order='F')
velocity = np.zeros(shape=10, dtype=float, order='F')
acceleration = np.zeros(shape=10, dtype=float, order='F')
time = np.zeros(shape=10, dtype=float, order='F')

space[0] = so
velocity[0] = vo

i = 0

while True:

    acceleration[i] = a
    velocity[i] = velocity[0] + acceleration[i]*i
    space[i] = space[0] + velocity[i]*i + (acceleration[i]*i**2)/2
    time[i] = i

    i = i + 1
    if i >= 10:
        break


plt.figure()

plt.xlabel("Time (s)")
plt.ylabel("Distance (m)")
plt.plot(time, space)
plt.show()

plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.plot(time, velocity)
plt.show()

plt.xlabel('Time (s)')
plt.ylabel('acceleration (m/s²)')
plt.plot(time, acceleration)
plt.show()

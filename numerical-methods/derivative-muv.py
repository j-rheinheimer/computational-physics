""" Programa derivada. """

import matplotlib.pyplot as plt
import numpy as np

so = float(input("Insira o espaço inicial: "))
vo = float(input("Insira a velocidade inicial: "))
a = float(input("Insira a aceleração: "))
# n = int(input('Insira o passo do tempo: '))

acceleration = np.zeros(shape=11, dtype=float, order='F')
velocity = np.zeros(shape=11, dtype=float, order='F')
space = np.zeros(shape=11, dtype=float, order='F')
time = np.zeros(shape=11, dtype=float, order='F')
dspace = np.zeros(shape=11, dtype=float, order='F')
dtime = np.zeros(shape=11, dtype=float, order='F')


def derivada(i):
    dspace[i] = space[i + 1] - space[i]
    dtime[i] = time[i + 1] - time[i]
    velocity[i] = dspace[i]/dtime[i]
    return velocity


acceleration[0] = a
velocity[0] = vo
space[0] = so
dt = 0
t = 1

for t in range(0, 10):
    dt = dt + 0.01
    time[t] = dt
    acceleration[t] = a
    space[t] = space[0] + velocity[t]*time[t] + (acceleration[t]*time[t]**2)/2
    derivada(t)

print(space, '\n', velocity, '\n', time)

plt.figure()

plt.ylabel('Space (m)')
plt.xlabel('Time (s)')
plt.plot(time, space)
plt.show()

plt.ylabel('Velocity (m/s)')
plt.xlabel('Time (s)')
plt.plot(time, derivada)
plt.show()

plt.ylabel('Acceleration (m/s²)')
plt.xlabel('TIme (s)')
plt.plot(time, acceleration)
plt.show()

import math
import numpy as np
import matplotlib.pyplot as plt

theta = np.zeros(100, dtype=float)
omega = np.zeros(100, dtype=float)
force = np.zeros(100, dtype=float)
time = np.zeros(100, dtype=float)

ang = float(input('Insira o valor do ângulo inicial: '))
wo = float(input('Insira a velocidade angular inicial: '))

theta[0] = math.radians(ang)
omega[0] = wo

g = float(input('Insira a gravidade local: '))
comp = float(input('Insira o comprimento do pêndulo: '))

dt = 0.05
i = 1

while True:

    omega[i] = omega[i - 1] - (g/comp)*theta[i - 1]*dt
    theta[i] = theta[i - 1] + omega[i-1]*dt
    time[i] = i

    i = i + 1
    if i >= 100:
        break

plt.figure()
plt.title('Theta x Time')
plt.ylabel('Theta (rad)')
plt.xlabel('Time (s)')
plt.plot(time, theta)
plt.show()

plt.figure()
plt.title('Omega x Time')
plt.ylabel('Omega (rad/s)')
plt.xlabel('Time (s)')
plt.plot(time, omega)
plt.show()

""" Packages imports """
import math
import numpy as np
import matplotlib.pyplot as plt

ANG = float(input("Insira o valor do ângulo de lançamento: "))
THETA = math.radians(ANG)

VO = float(input("Insira o módulo da velocidade de lançamento: "))

N = int(input('Insira o passo do tempo: '))

X = np.zeros(N, dtype=float, order='F')
Y = np.zeros(N, dtype=float, order='F')
VX = np.zeros(N, dtype=float, order='F')
VY = np.zeros(N, dtype=float, order='F')
TIME = np.zeros(N, dtype=float, order='F')

VX[0] = VO*math.cos(THETA)
VY[0] = VO*math.sin(THETA)
X[0] = 0
Y[0] = 0

DT = 0.05
T = 1

while True:
    TIME[T] = T*DT
    VX[T] = VX[T - 1]
    VY[T] = VY[T - 1] - 9.8*DT
    X[T] = X[T - 1] + VX[T]*DT
    Y[T] = Y[T - 1] + VY[T]*DT

    T = T + 1
    if T >= N:
        break


plt.figure()

plt.title("Y x X")
plt.ylabel("Y Distance (m)")
plt.xlabel("X Distance (m)")
plt.plot(X, Y, color="black")
plt.show()

plt.title("Vy x  Time")
plt.ylabel("Y Velocity (m/s)")
plt.xlabel("Time (s)")
plt.plot(TIME, VY, color="red")
plt.show()

plt.title("Vx x Time")
plt.ylabel("X Velocity (m/s)")
plt.xlabel("Time (s)")
plt.plot(TIME, VX, color="green")
plt.show()

print(X, '\n', Y, '\n', VX, '\n', VY, '\n', TIME)

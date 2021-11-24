import matplotlib.pyplot as plt
import numpy as np

velocity = np.zeros(10000)
space = np.zeros(10000)
time = np.zeros(10000)

k1 = np.zeros(10000)
k2 = np.zeros(10000)

l1 = np.zeros(10000)
l2 = np.zeros(10000)

h = 0.001
mass = 1
k = 1

time[0] = 0
space[0] = 1
velocity[0] = 0

for i in range(1, 10000):
    k1[i - 1] = h * ((-k / mass) * space[i - 1])
    k2[i - 1] = h * ((-k / mass) * (space[i - 1] + (h / 2)))
    velocity[i] = velocity[i - 1] + (1 / 6) * (k1[i - 1] + (2 * k2[i - 1]))

    l1[i - 1] = h * (velocity[i - 1])
    l2[i - 1] = h * (velocity[i - 1] + (h / 2))
    space[i] = space[i - 1] + (1 / 6) * (l1[i - 1] + (2 * l2[i - 1]))

    time[i] = time[i - 1] + (h * i)

plt.subplot(1, 2, 1)
plt.title("Space x Time")
plt.xlabel("Time (s)")
plt.ylabel("Space (m)")
plt.plot(time, space)

plt.subplot(1, 2, 2)
plt.title("Velocity x Time")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.plot(time, velocity)

plt.show()

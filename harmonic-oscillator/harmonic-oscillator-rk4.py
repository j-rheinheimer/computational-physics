import matplotlib.pyplot as plt
import numpy as np

vector_position = np.zeros(1000)
vector_velocity = np.zeros(1000)
vector_time = np.zeros(1000)

vector_derivative_1 = np.zeros(1000)
vector_derivarive_2 = np.zeros(1000)

vector_k1 = np.zeros(1000)
vector_k2 = np.zeros(1000)
vector_k3 = np.zeros(1000)
vector_k4 = np.zeros(1000)
vector_t4_1 = np.zeros(1000)

vector_l1 = np.zeros(1000)
vector_l2 = np.zeros(1000)
vector_l3 = np.zeros(1000)
vector_l4 = np.zeros(1000)
vector_t4_2 = np.zeros(1000)

const_mass = 1
const_k = 1

const_h = 0.001

vector_position[0] = 1
vector_velocity[0] = 0
vector_time[0] = 0


for i in range(1, 1000):
    vector_k1[i - 1] = (-const_k / const_mass) * vector_position[i - 1]
    vector_k2[i - 1] = (-const_k / const_mass) * (vector_position[i - 1] + (const_h / 2))
    vector_k3[i - 1] = (-const_k / const_mass) * (vector_position[i - 1] + (const_h / 2))
    vector_k4[i - 1] = (-const_k / const_mass) * (vector_position[i - 1] + const_h)
    vector_t4_1[i - 1] = (vector_k1[i - 1] + (2 * vector_k2[i - 1]) + (2 * vector_k3[i - 1]) + vector_k4[i - 1]) / 6

    vector_velocity[i] = vector_velocity[i - 1] + (const_h * vector_t4_1[i - 1])

    vector_time[i] = vector_time[i - 1] + const_h

print(vector_time, vector_velocity)

plt.title("Harmonic Oscillator, Mass-Spring system")
plt.ylabel("Position (m)")
plt.xlabel("Time (s)")
plt.plot(vector_time, vector_velocity)
plt.show()

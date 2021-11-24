import matplotlib.pyplot as plt
import numpy as np

# Analytical method

vector_x_test = np.zeros(100)
vector_y_test = np.zeros(100)

const_slope = 0.001
vector_x_test[0] = 0
vector_y_test[0] = 0

i = 0
while True:
    vector_x_test[i] = vector_x_test[i - 1] + const_slope
    vector_y_test[i] = vector_x_test[i] ** 2

    i = i + 1
    if i >= 100:
        break

# Numerical method

vector_y = np.zeros(100)
vector_x = np.zeros(100)

vector_k1 = np.zeros(100)
vector_k2 = np.zeros(100)
vector_k3 = np.zeros(100)
vector_k4 = np.zeros(100)
vector_t4 = np.zeros(100)

const_h = 0.001
vector_x[0] = 1

i = 0
while True:
    vector_k1[i - 1] = 2 * vector_x[i - 1]
    vector_k2[i - 1] = 2 * (vector_x[i - 1] + (const_h / 2))
    vector_k3[i - 1] = 2 * (vector_x[i - 1] + (const_h / 2))
    vector_k4[i - 1] = 2 * (vector_x[i - 1] + const_h)
    vector_t4[i - 1] = vector_k1[i - 1] + 2 * vector_k2[i - 1] + 2 * vector_k3[i - 1] + vector_k3[i - 1]

    vector_x[i] = vector_x[i - 1] + const_h
    vector_y[i] = vector_y[i - 1] + (const_h / 6) * vector_t4[i - 1]

    i = i + 1
    if i >= 100:
        break

# Plotting

plt.subplot(1, 2, 1)
plt.title("Runge-Kutta method")
plt.xlabel("X label")
plt.ylabel("Y label")
plt.plot(vector_x, vector_y, "r")

plt.subplot(1, 2, 2)
plt.title("Analytical method")
plt.xlabel("X label")
plt.ylabel("Y label")
plt.plot(vector_x_test, vector_y_test, "b")

plt.show()

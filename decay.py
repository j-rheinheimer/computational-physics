import matplotlib.pyplot as plt
import numpy as np

nu = np.zeros(100, dtype=float)
time = np.zeros(100, dtype=float)
diff = np.zeros(100, dtype=float)

nu[0] = 100
tau = 1
dt = 0.05
t = 1

while True:
    diff[t - 1] = -nu[t - 1]/tau
    nu[t] = nu[t - 1] + diff[t - 1]*dt
    time[t] = t

    t = t + 1
    if t >= 100:
        break

print(nu, nu.size)

plt.xlabel("Time (s)")
plt.ylabel("Number of Nuclei")
plt.plot(nu, time)
plt.show()

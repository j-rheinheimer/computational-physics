"""
X = particle number
Y = temperature
Z = internal energy
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random


def random_particle_x(temperature):
    x = (3/2)*(1.38*10**(-23))*random.random()
    return x


def random_particle_y(temperature):
    y = (3/2)*(1.38*10**(-23))*random.random()
    return y


def random_particle_z(temperature):
    z = (3/2)*(1.38*10**(-23))*random.random()
    return z


x_position = []
y_position = []
z_position = []
temperature_range = 100
for i in range(temperature_range):
    particle_x = random_particle_x(temperature_range)
    x_position.append(particle_x)
    particle_y = random_particle_y(temperature_range)
    y_position.append(particle_y)
    particle_z = random_particle_z(temperature_range)
    z_position.append(particle_z)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.scatter(x_position, y_position, z_position)
plt.show()

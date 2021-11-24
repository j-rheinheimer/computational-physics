from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random


def particle_movement_x(time):
    """
    Generates a random movement in the X label

    Parameter:
    time (int): Time step

    Return:
    x (int): X position
    """
    x = 0
    directions = [1, -1]
    for i in range(time):
        x = x + random.choice(directions)
    return x


def particle_movement_y(time):
    """
    Generates a random movement in the Y label

    Parameter:
    time (int): Time step

    Return:
    y (int): Y position
    """
    y = 0
    directions = [1, -1]
    for i in range(time):
        y = y + random.choice(directions)
    return y


def particle_movement_z(time):
    """
    Generates a random movement in the Z label

    Parameter:
    time (int): Time step

    Return:
    z (int): Z position
    """
    z = 0
    directions = [1, -1]
    for i in range(time):
        z = z + random.choice(directions)
    return z


number_of_particles = 10000
time_step = 100
particles_position = []
particles_position_x = []
particles_position_y = []
particles_position_z = []

for i in range(number_of_particles):
    x_position = particle_movement_x(time_step)
    particles_position_x.append(x_position)
    y_position = particle_movement_y(time_step)
    particles_position_y.append(y_position)
    z_position = particle_movement_z(time_step)
    particles_position_z.append(z_position)
    particles_position.append((x_position, y_position, z_position))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.scatter(particles_position_x, particles_position_y, particles_position_z)
plt.show()

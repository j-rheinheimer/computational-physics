from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random


class Gas():
    """
    Class that makes the simulation of a monoatomic gas
    """
    def __init__(self, temperature, number_of_particles, time):
        self.temperature = temperature
        self.number_of_particles = number_of_particles
        self.time = time

    def particle_movement_x(self, time):
        """
        Generates a random movement in the X label

        Parameter:
        time (int): Time step

        Return:
        x (int): X position
        """
        x = 0
        x_directions = [1, -1]
        for i in range(time):
            x = x + random.choice(x_directions)
        return x

    def particle_movement_y(self, time):
        """
        Generates a random movement in the Y label

        Parameter:
        time (int): Time step

        Return:
        y (int): Y position
        """
        y = 0
        y_directions = [1, -1]
        for i in range(time):
            y = y + random.choice(y_directions)
        return y

    def particle_movement_z(self, time):
        """
        Generates a random movement in the Z label

        Parameter:
        time (int): Time step

        Return:
        z (int): Z position
        """
        z = 0
        z_directions = [1, -1]
        for i in range(time):
            z = z + random.choice(z_directions)
        return z


gas_1 = Gas(100, 1000, 1000)
gas_1_particles_position = []
gas_1_particles_position_x = []
gas_1_particles_position_y = []
gas_1_particles_position_z = []

for i in range(gas_1.number_of_particles):
    gas_1_x_position = gas_1.particle_movement_x(gas_1.time)
    gas_1_particles_position_x.append(gas_1_x_position)
    gas_1_y_position = gas_1.particle_movement_y(gas_1.time)
    gas_1_particles_position_y.append(gas_1_y_position)
    gas_1_z_position = gas_1.particle_movement_z(gas_1.time)
    gas_1_particles_position_z.append(gas_1_z_position)
    gas_1_particles_position.append((
        gas_1_x_position,
        gas_1_y_position,
        gas_1_z_position))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.scatter(
    gas_1_particles_position_x,
    gas_1_particles_position_y,
    gas_1_particles_position_z)
plt.show()

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

constant = (3/2)*1.38*10**(-23)

particles_number = [0 for x in range(4)]
temperature = [0 for x in range(4)]
# X = rows, Y = columns
energy = ([[0 for y in range(4)] for x in range(4)])

for x in range(1, 4):  # row
    particles_number[x] = x
    for y in range(1, 4):  # column
        temperature[y] = y
        internal_energy = constant*temperature[y]*particles_number[x]
        energy[x][y] = internal_energy

print(temperature)
print(particles_number)
print(energy)

# print(energy)

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.set_xlabel('Particles number')
# ax.set_ylabel('Temperature')
# ax.set_zlabel('Internal energy')
# ax.scatter()

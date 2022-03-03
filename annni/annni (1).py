import numpy as np

n, m = 4, 4

identity = np.identity(2)

spin_x = np.array([[0, 1], [1, 0]])
spin_y = np.array([[0, -1j], [1j, 0]])
spin_z = np.array([[1, 0], [0, -1]])

matrix_one = np.ones((n, m))
matrix_two = np.ones((n, m))
matrix_three = np.ones((n, m))

# First interaction
i = 0
for j in range(0, m):
    if j == (m - 1):
        break
    else:
        matrix_one[i][j] = 2
        matrix_one[i][j + 1] = 2

    matrix_one[n - 1][0] = 2
    matrix_one[n - 1][3] = 2

    i = i + 1
    if i >= n:
        break

# Second interaction
i = 0
for j in range(0, m):
    if j == (m - 2):
        break
    else:
        matrix_two[i][j] = 2
        matrix_two[i][j + 2] = 2

    matrix_two[n - 2][2] = 2
    matrix_two[n - 2][0] = 2
    matrix_two[n - 1][3] = 2
    matrix_two[n - 1][1] = 2

    i = i + 1
    if i >= n:
        break

# Third interaction
i = 0
for j in range(0, m):
    if i == j:
        matrix_three[i][j] = 2

    i = i + 1
    if i >= n:
        break

for x in range(0, n):
    for y in range(0, m):
        if matrix_one[x][y] == 2:
            matrix_one[x][y] = spin_z
        else:
            matrix_one[x][y] = identity

        if matrix_two[x][y] == 2:
            matrix_two[x][y] = spin_z
        else:
            matrix_two[x][y] = identity

        if matrix_three[x][y] == 2:
            matrix_three[x][y] = spin_x
        else:
            matrix_three[x][y] = identity

print(matrix_one)
print(matrix_two)
print(matrix_three)

""" POO MUV e MU. """

import matplotlib.pyplot as plt
import numpy as np

N = int(input('Insira o o passo do tempo: '))


class MUV():

    """ Classe movimento uniformemente variado """

    smuv = np.zeros(shape=N, dtype=float, order='F')
    vmuv = np.zeros(shape=N, dtype=float, order='F')
    amuv = np.zeros(shape=N, dtype=float, order='F')
    tmuv = np.zeros(shape=N, dtype=float, order='F')

    def __init__(self, somuv, vomuv, aomuv):
        self.smuv[0] = somuv
        self.vmuv[0] = vomuv
        self.aomuv = aomuv

    def space_vectormuv(self, i):
        """ Vetor espaço MUV """
        self.smuv[i] = self.smuv[0] + self.vmuv[i]*i + (self.aomuv*(i**2))/2
        return self.smuv

    def velocity_vectormuv(self, i):
        """ Vetor velocidade MUV """
        self.vmuv[i] = self.vmuv[0] + self.aomuv*i
        return self.vmuv

    def aceleration_vectormuv(self, i):
        """ Vetor aceleração MUV """
        self.amuv[i] = self.aomuv
        return self.amuv

    def time_vectormuv(self, i):
        """ Vetor tempo MUV """
        self.tmuv[i] = i
        return self.tmuv


class MU():

    """ Classe movimento uniforme """

    smu = np.zeros(shape=N, dtype=float, order='F')
    vmu = np.zeros(shape=N, dtype=float, order='F')
    tmu = np.zeros(shape=N, dtype=float, order='F')

    def __init__(self, somu, vomu):
        self.smu[0] = somu
        self.vomu = vomu

    def space_vectormu(self, i):
        """ Vetor espaço MU """
        self.smu[i] = self.smu[0] + self.vomu*i
        return self.smu

    def velocity_vector(self, i):
        """ Vetor velocidade MU """
        self.vmu[i] = self.vomu
        return self.vmu

    def time_vectormu(self, i):
        """ Vetor tempo MU """
        self.tmu[i] = i
        return self.tmu


MOV_1 = MUV(somuv=0, vomuv=0, aomuv=1)
MOV_2 = MU(somu=2, vomu=5)

j = 0

while True:
    S1 = MOV_1.space_vectormuv(j)
    V1 = MOV_1.velocity_vectormuv(j)
    A1 = MOV_1.aceleration_vectormuv(j)
    T1 = MOV_1.time_vectormuv(j)

    """ Dados MU """
    S2 = MOV_2.space_vectormu(j)
    V2 = MOV_2.velocity_vector(j)
    T2 = MOV_2.time_vectormu(j)

    j = j + 1
    if j >= N:
        break

plt.figure()
plt.title("Space x Time")
plt.ylabel("Space (m)")
plt.xlabel("Time (s)")
plt.plot(T1, S1)
plt.show()

plt.figure()
plt.title("Velocity x Time")
plt.ylabel("Velocity (m/s)")
plt.xlabel("Time (s)")
plt.plot(T1, V1)
plt.show()

plt.figure()
plt.title('Aceleration x Time')
plt.ylabel('Aceleration (m/s²)')
plt.xlabel('Time (s)')
plt.plot(T1, A1)
plt.show()

plt.figure()
plt.title("Space x Time")
plt.ylabel("Space (m)")
plt.xlabel("Time (s)")
plt.plot(T2, S2)
plt.show()

plt.figure()
plt.title('Velocity x Time')
plt.ylabel('Velocity (m/s)')
plt.xlabel('Time (s)')
plt.plot(T2, V2)
plt.show()

print(S1, '\n', V1, '\n', A1, '\n', S2, '\n', V2, '\n', T1)

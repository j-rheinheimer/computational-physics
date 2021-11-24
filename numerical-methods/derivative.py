import math
import numpy as np
import matplotlib.pyplot as plt

dy = np.zeros(shape=100, dtype=float)
dx = np.zeros(shape=100, dtype=float)
diff = np.zeros(shape=100, dtype=float)

y = np.zeros(shape=100, dtype=float)

x = np.zeros(shape=100, dtype=float)

print('Tipos de funções:')
print(
    '-> Primeiro grau'
    '\n'
    'y(x) = a*x + b'
    '\n'
    '\n'
    '-> Segundo grau'
    '\n'
    'y(x) = a*(x**2) + b*x + c'
    '\n'
    '\n'
    '-> Terceiro grau'
    '\n'
    'y(x) = a*(x**3) + b*(x**2) + c*x + d'
    '\n'
    '\n'
    '-> Seno'
    '\n'
    'y(x) = a*sin(b*x)'
    '\n'
    '\n'
    '-> Cosseno'
    '\n'
    'y(x) = a*cos(b*x)'
    '\n'
    '\n'
    '-> Tangente'
    '\n'
    'y(x) = a*tan(b*x)'
    '\n'
)

function = input(
    'Insira o tipo da função que você deseja derivar'
    '\n'
    '(De a  cordo com o modelo acima): '
)

t = 1
cont = 1

if function == "Primeiro grau":
    a = float(input('Insira o valor do parametro a: '))
    b = float(input('Insira o valor do parametro b: '))

    while True:
        x[t] = cont
        y[t] = a*cont + b
        dy[t] = y[t] - y[t - 1]
        dx[t] = x[t] - x[t - 1]
        diff[t] = dy[t]/dx[t]

        cont = cont + 0.01
        t = t + 1
        if t >= 10:
            break


elif function == 'Segundo grau':
    a = float(input('Insira o valor do parametro a: '))
    b = float(input('Insira o valor do parametro b: '))
    c = float(input('Insira o valor do parametro c: '))

    while True:
        x[t] = cont
        y[t] = a*(cont**2) + b*cont + c
        dy[t] = y[t] - y[t - 1]
        dx[t] = x[t] - x[t - 1]
        diff[t] = dy[t]/dx[t]

        cont = cont + 0.01
        t = t + 1
        if t >= 10:
            break


elif function == 'Terceiro grau':
    a = float(input('Insira o valor do parametro a: '))
    b = float(input('Insira o valor do parametro b: '))
    c = float(input('Insira o valor do parametro c: '))
    d = float(input('Insira o valor do parametro d: '))

    while True:
        x[t] = cont
        y[t] = a*(cont**3) + b*(cont**2) + c*cont + d
        dy[t] = y[t] - y[t - 1]
        dx[t] = x[t] - x[t - 1]
        diff[t] = dy[t]/dx[t]

        cont = cont + 0.01
        t = t + 1
        if t >= 10:
            break


elif function == 'Seno':
    a = float(input('Insira o valor do parametro a: '))
    b = float(input('Insira o valor do parametro b: '))

    while True:
        x[t] = cont
        y[t] = a*math.sin(b*cont)
        dy[t] = y[t] - y[t - 1]
        dx[t] = x[t] - x[t - 1]
        diff[t] = dy[t]/dx[t]

        cont = cont + 0.01
        t = t + 1
        if t >= 10:
            break


elif function == 'Cosseno':
    a = float(input('Insira o valor do parametro a: '))
    b = float(input('Insira o valor do parametro b: '))

    while True:
        x[t] = cont
        y[t] = a*math.cos(b*cont)
        dy[t] = y[t] - y[t - 1]
        dx[t] = x[t] - x[t - 1]
        diff[t] = dy[t]/dx[t]

        cont = cont + 0.01
        t = t + 1
        if t >= 10:
            break


elif function == 'Tangente':
    a = float(input('Insira o valor do parametro a: '))
    b = float(input('Insira o valor do parametro b: '))

    while True:
        x[t] = cont
        y[t] = a*math.tan(b*cont)
        dy[t] = y[t] - y[t - 1]
        dx[t] = x[t] - x[t - 1]
        diff[t] = dy[t]/dx[t]

        cont = cont + 0.01
        t = t + 1
        if t >= 10:
            break

else:
    print('Você não digitou uma função válida')


plt.figure()

plt.title('Y x X')
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x, y)
plt.show()

plt.title('diff Y x X')
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x, diff)
plt.show()

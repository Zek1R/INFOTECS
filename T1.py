import matplotlib.pyplot as plt 
from math import sin
from math import cos
from math import pi


def X(v0, a, t):
    return v0 * cos(a) * t


def Y(v0, a, t):
    return v0 * sin(a) * t - 9.81*t**2/2


v0 = float(input('Введите начальную скорость (Vo) = '))

a = float(input('Введите начальный угол (α) = ')) * pi / 180

T = 2 * v0 * sin(a) / 9.81
print(f'Время полета {T}')

t_list = []
t = 0
k = 0
while t <= T and k < 1000000:
    t_list.append(t)
    t += 0.0001
    k+=1
t_list.append(T)

x_list = [X(v0, a, t) for t in t_list]
y_list = [Y(v0, a, t) for t in t_list]



print(f"Точка падения камня ({x_list[-1]}, {y_list[-1]})")
plt.grid()
plt.plot(x_list, y_list, c='b')
plt.show()
print("Количество значений -", len(t_list))
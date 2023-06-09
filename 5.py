from math import *
def f(y):
    s = 0
    n = len(y)
    for i in range(n):
        n1 = i // 2
        s += (y[i] ** 2 + 98 * y[n1] ** 3 + y[n1]) ** 5
    return s * 99

"""print(f([0.15, 0.69, 0.43, -0.32, -0.53, 0.72, 0.28, -0.22]))
print(f([0.81, -0.8, 0.55, 0.13, 0.83, -0.99, 0.85, 0.22]))
print(f([0.22, -0.29, 0.44, -0.06, -0.75, -0.07, -0.49, -0.87]))
print(f([0.95, -0.12, 0.83, 0.43, 0.47, 0.68, -0.12, -0.99]))
print(f([-0.34, -0.67, 0.82, -0.54, -0.79, 0.16, 0.15, -0.56]))"""

def f1(x):
    s = 0
    n = len(x)
    for i in range(n):
        s += ceil(1 + x[n - i - 1] + (x[n - i - 1]) ** 3) ** 3
    return s * 29

"""print(f1([-0.33, -0.3, 0.99, 0.64, -0.23, 0.25, 0.27, 0.23]))
print(f1([0.23, -0.61, -0.57, -0.68, 0.03, -0.61, 0.58, -0.01]))
print(f1([0.74, -0.12, -0.47, 0.41, -0.26, 0.56, 0.09, -0.35]))
print(f1([-0.94, -0.04, 0.75, -0.82, 0.37, -0.25, -0.2, -0.37]))
print(f1([-0.66, -0.9, -0.84, -0.28, -0.47, -0.64, 0.39, 0.63]))"""


def maxim(x, y):
    n = len(x)
    s = 0
    for i in range(n):
        s += (z[i] ** 3 - (x[n - i - 1] / 96)) ** 3 / 85
    return s * 81

import sympy as sp
import numpy as np
from math import factorial

x = sp.symbols('x')
X = sp.symbols('x')


def taylor(f, x0, n):
    x = sp.symbols('x')
    p = 0
    for k in range(0, n + 1):
        df = sp.diff(f, x, k)
        df_x0 = df.evalf(subs={x: x0})
        T = (df_x0 * (x - x0) ** k) / factorial(k)
        p = p + T
    return p


def biseccion(f, a, b, tol):
    if (f(a) * f(b) > 0):
        return '', 'La función no cumple el teorema en el intervalo'
    else:
        i = 0
        while (np.abs(b - a > tol)):
            c = (a + b) / 2
            if (f(a) * f(c) < 0):
                b = c
                i += 1
            else:
                a = c
                i += 1

    return c, i


def pos_falsa(f, a, b, tol):
    if (f(a) * f(b) > 0):
        print(f"La función no cumple el teorema en el intervalo {[a, b]}.")
        return False, False
    else:
        c = a - ((f(a) * (a - b)) / (f(a) - f(b)))
        count = 0
        while (np.abs(f(c)) > tol):
            c = a - ((f(a) * (a - b)) / (f(a) - f(b)))
            if (f(a) * f(c) < 0):
                b = c
            else:
                a = c
            count += 1
    return c, count


def datosTrapecio(xd, yd):
    h = xd[1] - xd[0]
    S = sum(yd) - yd[0] - yd[-1]
    I = (h / 2) * (yd[0] + yd[-1] + 2 * S)
    return I


def Newton(f, xo, tol):
    x = sp.symbols('x')
    df = sp.diff(f, x)
    N = x - f / df
    N = sp.lambdify(x, N)
    x1 = N(xo)
    count = 0
    while (np.abs(x1 - xo) > tol):
        count += 1
        xo = x1
        x1 = N(xo)
    return x1, count


def Secante(f, xo, x1, tol):
    x2 = x1 - f(x1) * (xo - x1) / (f(xo) - f(x1))
    count = 0
    while (np.abs(x2 - x1) > tol):
        count += 1
        xo = x1
        x1 = x2
        x2 = x1 - f(x1) * (xo - x1) / (f(xo) - f(x1))
    return x2, count


def Cota_t(f, x_, n, xo):
    df = sp.diff(f, x, n + 1)
    df = sp.lambdify(x, df)
    u = np.linspace(min(x_, xo), max(x_, xo), 1000)
    Max = np.max(np.abs(df(u)))
    cota = Max * ((x_ - xo) ** 4) / factorial(n + 1)
    return cota


def polinomial_simple(xdata, ydata):
    x = sp.symbols("x")
    N = len(xdata)
    Mat = np.zeros([N, N])
    P = 0
    Ps = 0
    for i in range(N):
        Mat[i, 0] = 1
        for j in range(1, N):
            Mat[i, j] = Mat[i, j - 1] * xdata[i]
    # a_i son los coeficientes del polinomio -> P(x) = a_0 + a_1x + a_2x**2  ; a_i
    a_i = np.linalg.solve(Mat, ydata)
    u = np.linspace(min(xdata), max(xdata), 1000)
    for i in range(N):
        P = P + a_i[i] * u ** i
        Ps = Ps + a_i[i] * x ** i
    return P, Ps


def lagrange(xdata, ydata):
    x = sp.symbols("x")
    N = len(xdata)
    P = 0
    for i in range(N):
        T = 1
        for j in range(N):
            if j != i:
                T *= (x - xdata[j]) / (xdata[i] - xdata[j])
        P = P + T * ydata[i]
    Ps = sp.lambdify(x, P)
    return P, Ps


def mc(xd, yd):
    m = len(xd)
    sy = sum(yd)
    sx = sum(xd)
    sxy = sum(xd * yd)
    dsx = sum(xd ** 2)
    sx2 = sx ** 2
    a0 = ((sy * dsx) - (sx * sxy)) / ((m * dsx) - sx2)
    a1 = ((m * sxy) - (sx * sy)) / ((m * dsx) - sx2)
    return a0, a1


def Euler(f, a, b, h, co):
    n = int((b - a) / h)
    t = np.linspace(a, b, n + 1)
    yeu = [co]
    for i in range(n):
        yeu.append(yeu[i] + h * f(t[i], yeu[i]))
    return t, yeu


def Runge4(f, a, b, h, co):
    n = int((b - a) / h)
    t = np.linspace(a, b, n + 1)
    yk = [co]
    for i in range(n):
        k1 = h * f(t[i], yk[i])
        k2 = h * f(t[i] + h / 2, yk[i] + 1 / 2 * k1)
        k3 = h * f(t[i] + h / 2, yk[i] + 1 / 2 * k2)
        k4 = h * f(t[i + 1], yk[i] + k3)
        yk.append(yk[i] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4))
    return t, yk


def Trapecio(f, a, b, n):
    h = (b - a) / n
    S = 0
    for i in range(1, n):
        S += f(a + i * h)
    I = h / 2 * (f(a) + 2 * S + f(b))
    return I


def sims13(f, a, b, n):
    if (n % 2 == 0):
        h = (b - a) / n
        Si = 0
        Sp = 0
        for i in range(1, n):
            if (i % 2 == 0):
                Sp += f(a + i * h)  # PARES
            else:
                Si += f(a + i * h)  # IMPARES
        I = (h / 3) * (f(a) + 2 * Sp + 4 * Si + f(b))
        return I
    else:
        print('Esta regla requiere un numero par de n')


def sims38(f, a, b, n):
    if (n % 3 == 0):
        h = (b - a) / n
        Si = 0
        Sp = 0
        for i in range(1, n):
            if (i % 3 == 0):
                Sp += f(a + i * h)  # MULTIPLOS DE 3
            else:
                Si += f(a + i * h)  # NO MULTIPLOS DE 3
        I = ((3 * h) / 8) * (f(a) + 2 * Sp + 3 * Si + f(b))
        return I
    else:
        print('Esta regla requiere un numero par de n')

"""Tabla 2: propiedades cuantitativas de funciones de activacion.
Momentos E[phi(z)^2] y E[phi'(z)^2] con z ~ N(0,1) por integracion numerica adaptativa
(scipy.integrate.quad, partida en z = 0 para las funciones no suaves en el origen);
supremo de |phi'| y minimo global sobre una malla fina en [-12, 12]."""
import numpy as np, csv
from scipy.special import erf

s = lambda x: 1/(1+np.exp(-x))
sp = lambda x: np.log1p(np.exp(-np.abs(x))) + np.maximum(x, 0)   # softplus estable
P = lambda x: 0.5*(1+erf(x/np.sqrt(2))); p = lambda x: np.exp(-x*x/2)/np.sqrt(2*np.pi)
LAM, ALP = 1.0507009873554805, 1.6732632423543772                  # constantes de SELU
F = {
 'Sigmoide': (s, lambda x: s(x)*(1-s(x))),
 'tanh': (np.tanh, lambda x: 1-np.tanh(x)**2),
 'ReLU': (lambda x: np.maximum(0, x), lambda x: (x > 0)*1.0),
 'ELU (a=1)': (lambda x: np.where(x > 0, x, np.expm1(np.minimum(x, 0))), lambda x: np.where(x > 0, 1.0, np.exp(np.minimum(x, 0)))),
 'SELU': (lambda x: LAM*np.where(x > 0, x, ALP*np.expm1(np.minimum(x, 0))), lambda x: LAM*np.where(x > 0, 1.0, ALP*np.exp(np.minimum(x, 0)))),
 'GELU': (lambda x: x*P(x), lambda x: P(x)+x*p(x)),
 'SiLU (b=1)': (lambda x: x*s(x), lambda x: s(x)*(1+x*(1-s(x)))),
 'Mish': (lambda x: x*np.tanh(sp(x)), lambda x: np.tanh(sp(x)) + x*s(x)*(1-np.tanh(sp(x))**2)),
}
from scipy.integrate import quad
phi = lambda z: np.exp(-z*z/2)/np.sqrt(2*np.pi)
E = lambda g: quad(lambda z: g(z)*phi(z), -np.inf, 0)[0] + quad(lambda z: g(z)*phi(z), 0, np.inf)[0]
grid = np.linspace(-12, 12, 2_400_001)
rows = []
for n, (f, df) in F.items():
    E2, Ed2 = E(lambda z: f(z)**2), E(lambda z: df(z)**2)
    fy = f(grid); i = np.argmin(fy)
    rows.append([n, round(float(np.max(np.abs(df(grid)))), 3), round(float(E2), 3), round(float(Ed2), 3), round(float(fy[i]), 3), round(float(grid[i]), 3)])
with open('resultados/tabla2_propiedades.csv', 'w', newline='') as fh:
    w = csv.writer(fh); w.writerow(['funcion', 'sup_abs_derivada', 'E_phi2', 'E_dphi2', 'minimo', 'z_minimo']); w.writerows(rows)
for r in rows: print(r)

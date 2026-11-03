"""Seccion 5: cociente log10(||grad W1|| / ||grad WL||) en la inicializacion.
MLP de L capas ocultas de ancho 128; 256 entradas gaussianas de dimension 128;
salida escalar lineal; perdida cuadratica; objetivo aleatorio; 5 semillas."""
import numpy as np, csv
from scipy.special import erf

def act(n):
    s = lambda x: 1/(1+np.exp(-x))
    if n == 'sigmoide': return s, lambda x: s(x)*(1-s(x))
    if n == 'tanh': return np.tanh, lambda x: 1-np.tanh(x)**2
    if n == 'relu': return lambda x: np.maximum(0, x), lambda x: (x > 0)*1.0
    if n == 'gelu':
        P = lambda x: 0.5*(1+erf(x/np.sqrt(2))); p = lambda x: np.exp(-x*x/2)/np.sqrt(2*np.pi)
        return lambda x: x*P(x), lambda x: P(x)+x*p(x)
    if n == 'silu': return lambda x: x*s(x), lambda x: s(x)*(1+x*(1-s(x)))

def cociente(n, L, seed, init, d=128, m=256):
    rng = np.random.default_rng(seed); f, df = act(n)
    X = rng.standard_normal((m, d)); y = rng.standard_normal((m, 1))
    dims = [d]+[128]*L+[1]; Ws = []
    for i in range(L+1):
        a, b = dims[i], dims[i+1]
        if init == 'glorot' or n in ('sigmoide', 'tanh'):
            lim = np.sqrt(6/(a+b)); Ws.append(rng.uniform(-lim, lim, (a, b)))   # Glorot uniforme
        else:
            Ws.append(rng.standard_normal((a, b))*np.sqrt(2/a))                # He normal
    hs, zs = [X], []
    for i in range(L):
        z = hs[-1] @ Ws[i]; zs.append(z); hs.append(f(z))
    delta = ((hs[-1] @ Ws[L]) - y)/m @ Ws[L].T; g = []
    for i in reversed(range(L)):
        dz = delta*df(zs[i]); g.append(np.linalg.norm(hs[i].T @ dz)); delta = dz @ Ws[i].T
    g = g[::-1]
    return float(np.log10(g[0]/g[-1]))

if __name__ == '__main__':
    rows = []
    for init in ('glorot', 'ajustada'):
        for n in ('sigmoide', 'tanh', 'relu', 'gelu', 'silu'):
            for L in (2, 5, 10, 20, 35, 50):
                v = [cociente(n, L, s, init) for s in range(5)]
                rows.append([init, n, L, round(float(np.mean(v)), 3), round(float(np.std(v)), 3)])
                print(rows[-1])
    with open('resultados/experimento_gradiente.csv', 'w', newline='') as fh:
        w = csv.writer(fh); w.writerow(['inicializacion', 'activacion', 'L', 'media_log10_cociente', 'desv_est']); w.writerows(rows)

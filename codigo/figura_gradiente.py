"""Fig. 2 a partir de resultados/experimento_gradiente.csv."""
import csv, collections
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
D = collections.defaultdict(list)
for r in csv.DictReader(open('resultados/experimento_gradiente.csv')):
    D[(r['inicializacion'], r['activacion'])].append((int(r['L']), float(r['media_log10_cociente'])))
fig, ax = plt.subplots(1, 2, figsize=(9, 3.4), sharey=True)
for k, (init, tit) in enumerate([('glorot', '(a) Glorot para todas'), ('ajustada', '(b) Glorot: σ, tanh; He: ReLU, GELU, SiLU')]):
    for n in ('sigmoide', 'tanh', 'relu', 'gelu', 'silu'):
        xs, ys = zip(*sorted(D[(init, n)])); ax[k].plot(xs, ys, marker='o', ms=3, label=n)
    ax[k].set_title(tit, fontsize=9); ax[k].set_xlabel('Profundidad L (capas ocultas)'); ax[k].grid(alpha=.3)
ax[0].set_ylabel('log10(‖∇W1‖/‖∇WL‖)'); ax[0].legend(fontsize=8)
plt.tight_layout(); plt.savefig('resultados/fig2_gradiente.png', dpi=300)

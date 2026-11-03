# Funciones de activación en la evolución de las RNA: material suplementario

Material suplementario del artículo *Las funciones de activación en la evolución de las redes neuronales artificiales: revisión histórico-conceptual y taxonomía cuantitativa*, de J. Jhayya Perlaza, C. M. Legón-Pérez y L. Bravo Ilisástegui, enviado a CCIA 2026.

## Contenido

| Carpeta | Archivo | Contenido |
| --- | --- | --- |
| `busqueda/` | `cadenas_busqueda.md` | Consultas, fechas, cifras y procedimiento de selección |
| `busqueda/` | `scopus_semillas_2026-11-03.csv` | Los 100 registros de la consulta de semillas (identificadores) |
| `busqueda/` | `scopus_control_2026-11-03.csv` | Los 15.244 registros de la búsqueda de control (identificadores) |
| `corpus/` | `cribado.csv` | Los 222 candidatos, con la propuesta preliminar, la decisión, el criterio y el consenso |
| `corpus/` | `muestra_segundo_autor.csv` | La clasificación ciega del segundo autor (20 candidatos) |
| `corpus/` | `corpus.csv` | Los 68 documentos del corpus, con su vía de entrada, su criterio y su número de referencia en el artículo |
| `codigo/` | `propiedades.py` | Calcula la Tabla 2 |
| `codigo/` | `experimento_gradiente.py` | Experimento de la Sección 5 |
| `codigo/` | `figura_gradiente.py` | Genera la Fig. 3 |
| `resultados/` | `*.csv`, `fig2_gradiente.png` | Salidas de los scripts (la figura corresponde a la Fig. 3 del artículo) |
| `resultados/` | `prisma_2020_en.png`, `prisma_2020_es.png` | Diagrama PRISMA 2020 de la selección (Fig. 1 del artículo), 1200 dpi |

Las exportaciones de Scopus solo incluyen identificadores bibliográficos. Los resúmenes y las listas de referencias no se redistribuyen.

## Reproducir los cálculos

Se necesita Python 3.10 o superior con `numpy`, `scipy` y `matplotlib`:

```bash
pip install numpy scipy matplotlib
python codigo/propiedades.py
python codigo/experimento_gradiente.py
python codigo/figura_gradiente.py
```

Ejecute los scripts desde la raíz del repositorio. No necesitan GPU ni datos externos.

## Uso de IA generativa

Durante el cribado, Claude (Anthropic) propuso una clasificación preliminar. Todas las decisiones las tomaron los autores. Los detalles están en `busqueda/cadenas_busqueda.md`.

## Licencia

Código: MIT. Datos de cribado y corpus: CC BY 4.0.

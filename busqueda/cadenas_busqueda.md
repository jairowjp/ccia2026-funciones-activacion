# Cadenas de búsqueda y registro

Todas las búsquedas se ejecutaron en Scopus el 3 de noviembre de 2026 con acceso institucional.

## 1. Selección de revisiones semilla

```
TITLE ( "activation function*" AND ( survey OR review OR comparison OR comparative OR benchmark OR overview ) ) AND PUBYEAR < 2025
```

- Registros: **100**. Exportación: `scopus_semillas_2026-11-03.csv`. Solo se publican los identificadores (EID, DOI, título, año, fuente y citas).
- Orden: *Cited by (highest)*. Semillas: las dos primeras.

| Semilla | Citas (3/11/2026) | Referencias según Scopus |
| --- | --- | --- |
| Dubey, Singh, Chaudhuri (2022), *Neurocomputing* 503 | 1.204 | 155 |
| Apicella, Donnarumma, Isgrò, Prevete (2021), *Neural Networks* 138 | 572 | 113 |
| **Total** | | **268** |

## 2. Bola de nieve hacia atrás (una iteración)

- La exportación de Scopus de las referencias produjo 244 entradas legibles, porque algunas aparecen fusionadas.
- Tras quitar 22 duplicados entre las dos semillas quedaron **222 candidatos únicos**.
- Resultado del cribado: **52 incluidos** y **170 excluidos**. Detalle en `../corpus/cribado.csv`.

| Motivo de exclusión | n |
| --- | --- |
| E1: tema ajeno (aplicación, arquitectura o datos) | 55 |
| E2: variante no adoptada (no está en PyTorch) | 96 |
| E3: duplicado | 13 |
| E4: libro de texto general | 6 |

**Procedimiento de selección.** Una herramienta de IA generativa (Claude, Anthropic) propuso una clasificación preliminar. El primer autor revisó y decidió cada caso. Un segundo autor clasificó a ciegas una muestra aleatoria de 20 candidatos, con una IA como apoyo y decisiones propias. El acuerdo fue de 17 de 20 (κ = 0,70). Las tres discrepancias (IDs 126, 165 y 194) se resolvieron por consenso; ver `../corpus/muestra_segundo_autor.csv` y la columna `nota_consenso`.

## 3. Búsqueda dirigida

Se añadieron 14 obras fundacionales y recientes que las semillas no citan. Las eligieron los autores y se verificaron en Scopus o arXiv. La lista está en `../corpus/corpus.csv` (vía = «Búsqueda dirigida»).

## 4. Control de cobertura

```
TITLE-ABS-KEY ( "activation function*" AND "neural network*" ) AND PUBYEAR < 2025
```

- Registros: **15.244**. Exportación: `scopus_control_2026-11-03.csv`, solo con los identificadores.
- Documentos del corpus recuperados: **24 de 68 (35 %)**:
  - 2 de 2 semillas;
  - 21 de 52 documentos de la bola de nieve;
  - 1 de 14 obras de la búsqueda dirigida.

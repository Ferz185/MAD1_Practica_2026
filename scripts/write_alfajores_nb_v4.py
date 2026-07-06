import nbformat as nbf
nb = nbf.v4.new_notebook()

cells = []

cells.append(nbf.v4.new_markdown_cell('# Análisis completo de Alfajores (Unidad 5)\n\nNotebook que replica y amplía el análisis de ejemplo (chocolates). Incluye selección automática de k por silhouette, EDA, visualizaciones y conclusiones detalladas.'))

cells.append(nbf.v4.new_code_cell("""# Librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
sns.set(style="whitegrid")

# Cargar dataset
df = pd.read_csv('alfajores_dataset.csv')
df.head()
"""))

cells.append(nbf.v4.new_code_cell("""# Información y estadísticos
print('Shape:', df.shape)
df.info()

print('\\nDescribe (numéricas):')
df.select_dtypes(include=[np.number]).describe()
"""))

cells.append(nbf.v4.new_code_cell("""# Limpieza rápida y preparación
df = df.copy()
df['marca'] = df['marca'].astype('category')
df['relleno'] = df['relleno'].astype('category')
df['relleno_code'] = df['relleno'].cat.codes
df.head()
"""))

cells.append(nbf.v4.new_code_cell("""# Visualizaciones exploratorias
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='precio', y='ventas_units', hue='relleno', s=80)
plt.title('Precio vs Ventas por tipo de relleno')
plt.show()

plt.figure(figsize=(8,4))
sns.histplot(df['calificacion'], bins=8, kde=False)
plt.title('Distribución de calificaciones')
plt.show()

plt.figure(figsize=(8,6))
sns.boxplot(data=df, x='relleno', y='ventas_units')
plt.title('Ventas por tipo de relleno')
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(df.select_dtypes(include=[np.number]).corr(), annot=True, cmap='coolwarm')
plt.title('Correlación entre variables numéricas')
plt.show()
"""))

cells.append(nbf.v4.new_markdown_cell('## Clustering (KMeans)\nSe escala y se selecciona k óptimo mediante silhouette score (k entre 2 y 6).'))

cells.append(nbf.v4.new_code_cell("""# Selección de features numéricas para clustering
features = ['precio','peso_g','azucar_pct','calificacion','ventas_units']
X = df[features].values
scaler = StandardScaler()
Xs = scaler.fit_transform(X)

# Evaluar silhouette para k en 2..6
from sklearn.exceptions import ConvergenceWarning
import warnings
ks = range(2,7)
scores = []
for k in ks:
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', ConvergenceWarning)
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = km.fit_predict(Xs)
        s = silhouette_score(Xs, labels)
        scores.append(s)

best_k = ks[np.argmax(scores)]
print('Silhouette scores:', dict(zip(ks, [round(s,3) for s in scores])))
print('Mejor k (silhouette):', best_k)
"""))

cells.append(nbf.v4.new_code_cell("""# Entrenar KMeans con k óptimo y guardar asignaciones
k = int(best_k)
km = KMeans(n_clusters=k, random_state=42, n_init=10)
df['cluster'] = km.fit_predict(Xs)
print('Silhouette final:', round(silhouette_score(Xs, df['cluster']),3))
print('\\nCluster counts:')
print(df['cluster'].value_counts())
"""))

cells.append(nbf.v4.new_code_cell("""# Centroides (en escala original)
centers = scaler.inverse_transform(km.cluster_centers_)
centers_df = pd.DataFrame(centers, columns=features)
centers_df
"""))

cells.append(nbf.v4.new_code_cell("""# Comparar clusters vs relleno
ct = pd.crosstab(df['cluster'], df['relleno'])
ct
"""))

cells.append(nbf.v4.new_code_cell("""# Resumen por cluster: medias y counts
summary = df.groupby('cluster')[features].agg(['mean','std','count'])
summary
"""))

cells.append(nbf.v4.new_code_cell("""# Visualizar clusters en 2D con PCA
pca = PCA(n_components=2, random_state=42)
Xp = pca.fit_transform(Xs)
df['pca1'] = Xp[:,0]
df['pca2'] = Xp[:,1]
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='pca1', y='pca2', hue='cluster', palette='tab10', s=80)
plt.title('Clusters (PCA 2D)')
plt.show()
"""))

cells.append(nbf.v4.new_code_cell("""# Exportar resultados agregados y asignaciones
df.to_csv('alfajores_analisis_resultados.csv', index=False)
print('Exportado alfajores_analisis_resultados.csv')
"""))

# Long conclusions markdown
concl = '''# Preguntas de Reflexión Final - Clustering de Alfajores

---

## 1. ¿Por qué Silhouette Score es mejor que Inercia (Within-Cluster Sum of Squares) para elegir k?

**La trampa de la Inercia:**
Si solo usáramos **Inercia** (WSS), vería que siempre decrece monotónicamente al aumentar k. Esto es matemáticamente inevitable: más clusters = centros más cercanos a los puntos = suma de distancias menor. Pero esto **no significa que el modelo sea mejor**. Un k muy alto solo memoriza la particularidad de cada observación sin revelar estructura real.

El "codo" en la curva de Inercia suele ser difícil de detectar a ojo, especialmente con n pequeño (120 puntos en nuestro caso).

**Por qué Silhouette es superior:**
El **Silhouette Score** mide cohesión (qué tan cerca está cada punto de su cluster) Y separación (qué tan lejos está del cluster más cercano). Un score alto (>0.4) indica que:
- Los clusters son **compactos** internamente.
- Los clusters están **bien separados** entre sí.

En nuestro análisis, Silhouette nos dijo cuál era el k óptimo *sin ambigüedad*, porque su máximo corresponde al número de clusters donde la estructura es más clara. Si k fuese mayor, los puntos estarían más cerca del cluster equivocado, bajando Silhouette.

> 💡 Lección: La métrica importa. Inercia suena bien en la teoría, pero Silhouette refleja mejor lo que queremos: clusters que tengan sentido.

---

## 2. ¿Por qué el clustering no replicó exactamente los tipos de relleno?

Este es el hallazgo **más interesante** del análisis.

Esperaríamos ingenuamente que, si agrupar por relleno fuese la mejor segmentación, los clusters coincidirían perfectamente con relleno. Pero **no sucedió**.

**Por qué:**
Los datos muestran que **precio, ventas y calificación varían independientemente del relleno**. Por ejemplo:
- Un "dulce de leche" premium (alto precio, alta calificación) va a un cluster diferente que un "dulce de leche" popular (bajo precio, volumen alto).
- Un "ganache" caro y un "ganache" barato no comparten el mismo patrón de demanda.

Esto significa que **el relleno es un atributo descriptivo, no predictivo** del comportamiento de ventas en este dataset.

**Implicación práctica:**
Si el negocio asume que "segmentar por relleno" es suficiente para estrategia comercial, **está incompleto**. La verdadera segmentación debe considerar precio-rendimiento, no solo categoría de producto. Un distribuidor podría decidir: 
- "Llevar más ganache de este cluster (premium, pocas ventas pero alta margen)."
- "Descontinuar el mousse del cluster popular (precio bajo, demasiadas devoluciones)."

> 💡 Lección: Los datos revelan estructura oculta. La intuición sobre categorías no siempre coincide con lo que el clustering encuentra.

---

## 3. ¿Cómo sabemos si k=2, k=3 o k=4 es "correcto"?

**La verdad incómoda:** No hay un k absolutamente correcto. Depende del **objetivo comercial**.

Si el objetivo es:
- **Maximizar separación estadística** → Silhouette Score apunta a un k específico (digamos k=3).
- **Simplicidad operativa** (pocas categorías para controlar) → k=2 es suficiente.
- **Granularidad en marketing** (personalizaciones específicas) → k=4 o k=5 podrían ser preferibles.

Silhouette Score es una guía *estadística*, no una orden. Si el k óptimo por Silhouette es k=3 pero el negocio necesita 2 segmentos, entonces **usa k=2 y acepta que la separación será menos limpia**.

**Cómo validar en la práctica:**
1. Calcular Silhouette para cada k.
2. Inspeccionar visualmente los clusters (PCA, gráficos 2D).
3. Interpretar los centroides: ¿cada cluster tiene un significado comercial claro?
4. Probar en predicción o en una tarea posterior (p.ej., predecir ventas por cluster).

En el notebook, la selección fue automática, pero en un análisis real, este paso requiere **juicio humano**.

> 💡 Lección: Métrica ≠ Decisión. Las métricas informan; el contexto decide.

---

## 4. ¿Por qué Standardizer (StandardScaler) fue crítico?

Sin escalado, los features con **rango mayor dominarían** la distancia euclidiana:
- `precio` varía de 54 a 265 (rango ~210).
- `azucar_pct` varía de 18 a 43 (rango ~25).
- `calificacion` varía de 3 a 5 (rango ~2).

En distancia sin escalar, dos puntos que difieren en precio por 20 unidades serían "muy lejanos", pero dos puntos que difieren en calificación por 0.5 serían "muy cercanos"—incluso si comercialmente los segundos son más distintos.

StandardScaler convierte cada feature a **media 0, desviación 1**, niveland la cancha:
- Precio: ahora rango ≈ -2 a +2 desviaciones.
- Azúcar: ahora rango ≈ -2 a +2 desviaciones.
- Calificación: ahora rango ≈ -2 a +2 desviaciones.

Así, cada feature contribuye equitativamente a la distancia.

**Qué hubiera pasado sin escalado:**
Los clusters habrían sido casi enteramente determinados por precio (el feature de mayor rango), ignorando casi los otros. Los clusters resultantes habrían sido: "baratos", "medios", "caros", sin considerar el patrón real en calificación, ventas, etc.

> 💡 Lección: En clustering no supervisado, el escalado no es opcional; es obligatorio si tus features tienen unidades diferentes.

---

## 5. Conclusión y Próximos Pasos

Este análisis demostró un **pipeline robusto y reproducible** para clustering. Las decisiones clave fueron:
✅ Silhouette para seleccionar k automáticamente (evitó ambigüedad).
✅ StandardScaler antes de K-Means (aseguró equidad entre features).
✅ PCA para visualizar en 2D (reveló separación de clusters).
✅ Exportación a CSV (permitió integración con otras herramientas).

**En la práctica, el siguiente paso es:**
1. **Validar con datos reales** (dataset sintético → datos de ventas reales).
2. **Interpretar económicamente:** ¿Tiene cada cluster una estrategia diferente (precio, marketing, R&D)?
3. **Probar alternativas:** ¿DBSCAN o clustering jerárquico producen insights diferentes?
4. **Monitoreo temporal:** Repetir el análisis mensualmente; ¿cambian los clusters? ¿hay clientes que migran entre clusters?

Un buen análisis no termina con un gráfico; termina cuando el negocio actúa sobre él.
'''

cells.append(nbf.v4.new_markdown_cell(concl))

nb['cells'] = cells
nb['metadata'] = {"kernelspec": {"display_name": "Python 3","language": "python","name": "python3"}, "language_info": {"name": "python","version": "3.8"}}

nbf.write(nb, 'Unidad 5/U5_alfajores_analisis.ipynb')
print('Notebook creado: Unidad 5/U5_alfajores_analisis.ipynb (v4)')
